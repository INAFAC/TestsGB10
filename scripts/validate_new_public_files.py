#!/usr/bin/env python3
"""Comprueba los archivos de trabajo antes de publicar."""
import argparse
import gzip
import pathlib
import re
import subprocess

ROOT=pathlib.Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--all", action="store_true", help="Incluir todos los archivos versionados")
options = parser.parse_args()
files=set()
if options.all:
    files.update(subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT, text=True).split("\0")[:-1])
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
checked=0
for name in sorted(files):
    p=ROOT/name
    if not p.is_file():continue
    checked+=1
    data=p.read_bytes()
    if p.suffix=='.gz':data=gzip.decompress(data)
    text=data.decode(errors='replace')
    for label,pattern in patterns.items():
        if re.search(pattern,text):errors.append(f'{name}: possible {label}')
if errors:raise SystemExit('\n'.join(errors))
print(f'Control de privacidad completado sobre {checked} archivos. Requiere además revisión manual.')
