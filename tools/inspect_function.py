"""Hash an ARM64 Mach-O function range and optionally compare after BL-only masking.
Inputs must be independently obtained; this tool neither downloads nor executes them.
"""
import argparse,hashlib,json,struct
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--binary',type=Path,required=True);p.add_argument('--expected-sha256',required=True);p.add_argument('--address',type=lambda s:int(s,0),required=True);p.add_argument('--size',type=int,required=True);p.add_argument('--compare-binary',type=Path);p.add_argument('--compare-sha256');p.add_argument('--compare-address',type=lambda s:int(s,0));a=p.parse_args()
def extract(path,expected,address,size):
 d=path.read_bytes();digest=hashlib.sha256(d).hexdigest()
 if digest!=expected:raise SystemExit('Binary hash mismatch')
 if d[:4]!=b'\xcf\xfa\xed\xfe' or struct.unpack_from('<I',d,4)[0]!=0x100000c:raise SystemExit('Expected little-endian ARM64 Mach-O')
 if size<=0 or size%4:raise SystemExit('Size must be a positive multiple of four')
 pos=32;span=None
 for _ in range(struct.unpack_from('<I',d,16)[0]):
  cmd,n=struct.unpack_from('<II',d,pos)
  if n<8 or pos+n>len(d):raise SystemExit('Invalid load command')
  if cmd==0x19:
   for j in range(struct.unpack_from('<I',d,pos+64)[0]):
    q=pos+72+j*80;name=d[q:q+16].split(b'\0')[0];base,length,off=struct.unpack_from('<QQI',d,q+32)
    if name==b'__text' and base<=address and address+size<=base+length:span=d[off+address-base:off+address-base+size]
  pos+=n
 if span is None or len(span)!=size:raise SystemExit('Range outside __text')
 words=struct.unpack('<'+'I'*(size//4),span);mask=b''.join(struct.pack('<I',w&0xfc000000 if w&0xfc000000==0x94000000 else w) for w in words)
 return {'binary_sha256':digest,'address':hex(address),'size':size,'body_sha256':hashlib.sha256(span).hexdigest(),'bl_normalized_sha256':hashlib.sha256(mask).hexdigest(),'masked_bl_instructions':sum(w&0xfc000000==0x94000000 for w in words)},span,mask
r,x,n=extract(a.binary,a.expected_sha256,a.address,a.size);result={'reference':r,'limit':'Selected range comparison; does not prove function boundaries, upstream-source equivalence, runtime use or copyright scope.'}
if a.compare_binary:
 if not a.compare_sha256 or a.compare_address is None:p.error('comparison needs --compare-sha256 and --compare-address')
 s,y,m=extract(a.compare_binary,a.compare_sha256,a.compare_address,a.size);result.update(comparison=s,exact_match=x==y,bl_normalized_match=n==m)
print(json.dumps(result,indent=2))
