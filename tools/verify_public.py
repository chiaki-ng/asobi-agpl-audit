"""Verify public snapshot hashes, text-only allowlist, local links and exposure checks."""
from pathlib import Path
import hashlib,json,re,subprocess
root=Path(__file__).resolve().parents[1];manifest=root/'SHA256SUMS';expected={}
for line in manifest.read_text().splitlines():
 digest,name=line.split('  ',1)
 if name in expected or Path(name).is_absolute() or '..' in Path(name).parts:raise SystemExit('Unsafe/duplicate manifest path')
 expected[name]=digest
files={str(p.relative_to(root)):p for p in root.rglob('*') if p.is_file() and not set(p.relative_to(root).parts)&{'.git','__pycache__'}}
if set(files)!=(set(expected)|{'SHA256SUMS'}):raise SystemExit('Manifest file set mismatch')
for name,digest in expected.items():
 p=files[name]
 if p.is_symlink():raise SystemExit('Symlink: '+name)
 b=p.read_bytes()
 if p.suffix=='.png':
  if not name.startswith(('evidence/ipa-exhibits/','evidence/github-screenshots/','evidence/reddit-screenshots/')) or b[:8]!=b'\x89PNG\r\n\x1a\n':raise SystemExit('Unexpected image: '+name)
 elif p.suffix not in {'.md','.json','.py','.asm','.txt',''} and name!='.gitignore':raise SystemExit('Unexpected file type: '+name)
 if hashlib.sha256(b).hexdigest()!=digest:raise SystemExit('Hash mismatch: '+name)
 if p.suffix=='.png':continue
 s=b.decode('utf-8')
 # Checker source contains its own patterns; evidence/docs must not contain their matches.
 if not name.startswith('tools/'):
  for pattern in [r'/(?:Users|home)/[^\s/]+',r'/private/(?:tmp|var)/',r'BEGIN [A-Z ]*PRIVATE KEY',r'(?i)e{1,2}ve{1,2}decryp',r'(?i)\bdecryp(?:ter|ting|ted)\b',r'(?i)\b(?:authorization: bearer|access_token=|refresh_token=)',r'(?i)[\w.+-]+@(?:proton\.me|gmail\.com|icloud\.com)']:
   if re.search(pattern,s):raise SystemExit('Exposure pattern: '+name)
 if p.suffix=='.json':json.loads(s)
 if p.suffix=='.md':
  for link in re.findall(r'\]\(([^)]+)\)',s):
   if link.startswith(('https://','http://','#','mailto:')):continue
   dest=(p.parent/link.split('#')[0]).resolve()
   if not dest.is_relative_to(root.resolve()) or not dest.exists():raise SystemExit('Broken/escaping link: '+name+' -> '+link)
if (root/'.git').exists():
 count=subprocess.check_output(['git','-C',str(root),'rev-list','--all','--count'],text=True).strip()
 remotes=subprocess.check_output(['git','-C',str(root),'remote'],text=True).strip()
 print('Git commits:',count,'Configured remote:',bool(remotes))
print('PASS:',len(expected),'manifest entries; exact file set, text types, links and exposure patterns checked.')
