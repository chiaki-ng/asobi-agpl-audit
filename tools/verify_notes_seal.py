"""Check that Markdown files in an Asobi store IPA are sealed by the app's Apple code signature.

Chain: the main executable's CodeDirectory special slot -3 holds the SHA-256 of _CodeSignature/CodeResources;
CodeResources (files2) holds the SHA-256 of each sealed resource. Reads the IPA only; nothing is executed,
and FairPlay encryption of the executable's code does not cover its code signature. Store-only metadata
(iTunesMetadata.plist, SC_Info) is never read.

    python3 tools/verify_notes_seal.py STORE.ipa [STORE.ipa ...] [--json OUT]
"""
import argparse,hashlib,json,plistlib,re,struct,sys,zipfile
CSMAGIC_EMBEDDED=0xfade0cc0;CSMAGIC_CD=0xfade0c02;LC_CODE_SIGNATURE=0x1d
def cd_special_slots(macho):
 """Return {hash_type: {slot: hex}} for every CodeDirectory in a thin or fat arm64 Mach-O."""
 magic=struct.unpack_from('>I',macho)[0];slices=[0]
 if magic in(0xcafebabe,0xcafebabf):
  n=struct.unpack_from('>I',macho,4)[0];w=20 if magic==0xcafebabe else 32
  slices=[struct.unpack_from('>I' if w==20 else '>Q',macho,8+i*w+(8 if w==20 else 8))[0] for i in range(n)]
 out={}
 for base in slices:
  m=struct.unpack_from('<I',macho,base)[0]
  if m!=0xfeedfacf:continue
  ncmds=struct.unpack_from('<I',macho,base+16)[0];off=base+32
  for _ in range(ncmds):
   cmd,size=struct.unpack_from('<II',macho,off)
   if cmd==LC_CODE_SIGNATURE:
    sigoff,_sz=struct.unpack_from('<II',macho,off+8);sb=base+sigoff
    assert struct.unpack_from('>I',macho,sb)[0]==CSMAGIC_EMBEDDED
    count=struct.unpack_from('>I',macho,sb+8)[0]
    for i in range(count):
     _t,boff=struct.unpack_from('>II',macho,sb+12+i*8);cd=sb+boff
     if struct.unpack_from('>I',macho,cd)[0]!=CSMAGIC_CD:continue
     hoff,_ident,nspecial=struct.unpack_from('>III',macho,cd+16)
     hsize,htype=macho[cd+36],macho[cd+37]
     out.setdefault(htype,{}).update({-k:macho[cd+hoff-k*hsize:cd+hoff-(k-1)*hsize].hex() for k in range(1,nspecial+1)})
   off+=size
 return out
def check(ipa):
 z=zipfile.ZipFile(ipa);names=z.namelist()
 app=[n for n in names if re.fullmatch(r'Payload/([^/]+)\.app/\1',n)][0];root=app.rsplit('/',1)[0]+'/'
 info=plistlib.loads(z.read(root+'Info.plist'))
 crb=z.read(root+'_CodeSignature/CodeResources');cr=plistlib.loads(crb)['files2']
 slots=cd_special_slots(z.read(app));sha256_slot=slots.get(2,{}).get(-3)
 notes={}
 for k in sorted(x for x in cr if x.lower().endswith('.md')):
  sealed=cr[k]['hash2'].hex() if isinstance(cr[k],dict) else None
  actual=hashlib.sha256(z.read(root+k)).hexdigest() if root+k in names else None
  notes[k]={'sha256':actual,'sealed_sha256':sealed,'match':actual==sealed}
 crh=hashlib.sha256(crb).hexdigest()
 return {'version':info.get('CFBundleShortVersionString'),'build':info.get('CFBundleVersion'),'bundle_id':info.get('CFBundleIdentifier'),
  'code_resources_sha256':crh,'signature_slot_minus3_sha256':sha256_slot,'code_resources_sealed':crh==sha256_slot,'markdown_notes':notes,
  'all_notes_sealed':crh==sha256_slot and all(n['match'] for n in notes.values())}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('ipa',nargs='+');p.add_argument('--json');a=p.parse_args()
 rows=[check(f) for f in a.ipa]
 for r in rows:print(r['version'],r['build'],'CodeResources sealed' if r['code_resources_sealed'] else 'CodeResources NOT sealed',len(r['markdown_notes']),'notes',('all sealed' if r['all_notes_sealed'] else 'MISMATCH') if r['markdown_notes'] else '')
 if a.json:json.dump(rows,open(a.json,'w'),indent=1)
 sys.exit(0 if all(r['code_resources_sealed'] and all(n['match'] for n in r['markdown_notes'].values()) for r in rows) else 1)
