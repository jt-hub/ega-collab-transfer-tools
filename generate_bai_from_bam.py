#!/usr/bin/env python

import argparse
import os
import subprocess
from shutil import copyfile

def main():
    try:
        # Parsing the command line arguments
        parser = argparse.ArgumentParser(description='Generate a bai file from BAM file')
        parser.add_argument('-i', '--input',  dest='input', help="Input BAM file", required=True)
        parser.add_argument('-o', '--output', dest="output", help="Name of the output BAI file", required=True)

        results = parser.parse_args()

        try:
            FNULL = open(os.devnull, 'w')
            subprocess.call(['samtools'], stdout=FNULL, stderr=subprocess.STDOUT)
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print "Error: samtools in not installed in the path"
                exit(1)

        if not os.path.isfile(results.input):
            raise ValueError("Input file does not exist: "+results.input)

        if os.path.isfile(results.output):
            raise ValueError("Output file already exists")

        subprocess.call(['samtools','index','-b',results.input])
        copyfile(results.input+".bai",results.output)
        os.remove(results.input + ".bai")
    except Exception, err:
        print err
        exit(1)

if __name__ == '__main__':
    main()
