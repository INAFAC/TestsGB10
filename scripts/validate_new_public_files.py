#!/usr/bin/env python3
"""Screen new or changed files before publication; existing reviewed data is untouched."""
import gzip
import pathlib
import re
import subprocess

ROOT=pathlib.Path(__file__).resolve().parents[1]
files=set()
for args in [['ls-files','--others','--exclude-standard'],['diff','--name-only'],['diff','--cached','--name-only']]:
    files.update(subprocess.check_output(['git',*args],cwd=ROOT,text=True).splitlines())
patterns={
    'personal home directory':r'/home/(?!usuario\b)[\w.-]+',
    'private IPv4 address':r'\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b',
    'GitHub credential':r'gh[pousr]_[A-Za-z0-9]{20,}',
    'authorization credential':r'(?i)Bearer\s+[A-Za-z0-9_-]{15,}',
    'private key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'credential assignment':r'(?i)(?:api_key|password|access_token)\s*[=:]\s*[\"\x27][^\"\x27]{8,}',
}
errors=[]
for name in sorted(files):
    p=ROOT/name
    if not p.is_file():continue
    data=p.read_bytes()
    if p.suffix=='.gz':data=gzip.decompress(data)
    text=data.decode(errors='replace')
    for label,pattern in patterns.items():
        if re.search(pattern,text):errors.append(f'{name}: possible {label}')
if errors:raise SystemExit('\n'.join(errors))
print(f'Privacy screen passed for {len(files)} new or modified files. This screen supplements manual review.')
