#!/usr/bin/env python3
"""Read-only environment preflight."""
from __future__ import annotations
import argparse, os, shutil, socket
from pathlib import Path
def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode', choices=('plan','status','preflight'), default='preflight'); a=p.parse_args(); home=Path(os.environ.get('HERMES_HOME', Path.home()/'.hermes')); root=home/'llm-routing'
    checks=[('python3', shutil.which('python3') is not None), ('hermes-home', home.exists()), ('selector', (Path(__file__).with_name('model-selection.py')).exists()), ('routing-port-free', _free(4000))]
    print({'capability':'llm-routing','mode':a.mode,'root':str(root),'checks':[{'name':n,'ok':ok} for n,ok in checks],'credentials_read':False,'activation':False})
def _free(port):
    with socket.socket() as s:
        try: s.bind(('127.0.0.1',port)); return True
        except OSError: return False
if __name__=='__main__': main()
