#!/usr/bin/env python3
"""Download the running campaign outside the repo, then publish readable test folders."""
import argparse
import pathlib
import subprocess
p=argparse.ArgumentParser()
p.add_argument('--host',default='CanadasGB10')
p.add_argument('--cache-dir',default=str(pathlib.Path.home()/'.cache/TestsGB10/campana-2026-10-14'))
p.add_argument('--publish',action='store_true')
p.add_argument('--message',default='Actualiza los resultados medidos del GB10')
a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1];cache=pathlib.Path(a.cache_dir)
for remote,local in [('/tmp/gb10-memory-20261014-1344','memory'),('/tmp/gb10-after30-20261014','after30'),('/tmp/gb10-reuse-20261014','reuse')]:
    destination=cache/local;destination.mkdir(parents=True,exist_ok=True)
    subprocess.run(['rsync','-az','--exclude=*.tmp',a.host+':'+remote+'/',str(destination)+'/'],check=True)
subprocess.run(['python3',str(root/'scripts/import_measurements.py'),'--source',str(cache)],cwd=root,check=True)
for script in ['build_report.py','validate_report.py']:
    subprocess.run(['python3',str(root/'scripts'/script)],cwd=root,check=True)
subprocess.run(['git','diff','--check'],cwd=root,check=True)
if a.publish:
    subprocess.run(['git','add','-A'],cwd=root,check=True)
    if subprocess.run(['git','diff','--cached','--quiet'],cwd=root).returncode:
        subprocess.run(['git','commit','-m',a.message],cwd=root,check=True)
    subprocess.run(['git','push'],cwd=root,check=True)
