#!/usr/bin/env python

import argparse
import os
from icgconnect.collab import quick_upload
import subprocess

def main():

    # Parsing the command line arguments
    parser = argparse.ArgumentParser(description='Upload a file to collab')
    parser.add_argument('-i', '--input', dest='input', help="Input file", required=True)
    parser.add_argument('-g', '--gnos-id', dest='gnos_id', help="GNOS ID", required=True)
    parser.add_argument('-id', '--object-id', dest="object_id", help="Id service token", required=True)
    parser.add_argument('-md5', '--md5-checksum', dest="md5", help="MD5 checksum", required=True)

    results = parser.parse_args()

    try:
        FNULL = open(os.devnull, 'w')
        subprocess.call(['icgc-storage-client'], stdout=FNULL, stderr=subprocess.STDOUT)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print "Error: icgc-storage-client in not installed in the path"
            exit(1)

    if not os.path.isfile(results.input):
        raise ValueError("Input file does not exist: " + results.input)

    _file = {'object_id':results.object_id,'file_md5sum':results.md5,'file_name':results.input}

    quick_upload(results.gnos_id, [_file], 'icgc-storage-client')


if __name__ == '__main__':
    main()