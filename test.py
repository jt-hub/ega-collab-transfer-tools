#!/usr/bin/env python

import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Generate a bai file from BAM file')
    parser.add_argument('-i', '--input',  dest='input', help="Input BAM file", required=True)
    parser.add_argument('-o', '--output', dest="output", help="Name of the output BAI file", required=True)

    results = parser.parse_args()
    print "input="+results.input
    print "output="+results.output

if __name__ == '__main__':
	main()
