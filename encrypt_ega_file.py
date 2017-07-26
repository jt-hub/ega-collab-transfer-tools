#!/usr/bin/env python

import argparse
import os
import subprocess

import hashlib

def get_md5(fname):
    hash = hashlib.md5()
    if not os.path.isfile(fname): return None
    with open(fname) as f:
        for chunk in iter(lambda: f.read(1024*256), ""):
            hash.update(chunk)
    return hash.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Encrypt EGA file and generate file with md5 checksum.')
    parser.add_argument('-f', '--file', dest="file", help="File to encrypt", required=True)

    results = parser.parse_args()

    encrypted_file = results.file+".gpg"
    encrypted_md5_file = results.file+".gpg.md5"
    unencrypted_md5_file = results.file+".md5"

    try:
        if not os.path.isfile(results.file):
            raise ValueError("Input file does not exists: "+results.file)

        subprocess.call(['gpg','--yes','--trust-model','always','-r','EGA_Public_Key','--encrypt',results.file])

        with open(encrypted_md5_file,"w") as text_file:
            text_file.write(get_md5(encrypted_file))

        with open(unencrypted_md5_file,"w") as text_file:
            text_file.write(get_md5(results.file))

    except Exception, err:
        print err
        exit(1)

if __name__ == "__main__":
    main()
