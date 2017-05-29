#!/usr/bin/env python

import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Encrypt file with openssl')
    parser.add_argument('-i', '--input', dest="input", help="File to encrypt", required=True)
    parser.add_argument('-o', '--output', dest="output", help="Output file", required=True)
    parser.add_argument('-k', '--key', dest="key", help="Encryption key", required=True)

    results = parser.parse_args()

    try:
        if not os.path.isfile(results.input):
            raise ValueError("Input file does not exists: "+results.input)

        if os.path.isfile(results.output):
            raise ValueError("Output file already exists: "+results.output)

        subprocess.call(['openssl','enc','-in',results.input,'-out',results.output,'-e','-aes-256-cbc','-k',results.key])

    except Exception, err:
        print err
        exit(1)

if __name__ == "__main__":
    main()
