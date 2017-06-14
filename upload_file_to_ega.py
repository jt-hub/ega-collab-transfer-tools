#!/usr/bin/env python

import argparse
import subprocess
import os

def main():
    # Parsing of the input parameters using argparse
    parser = argparse.ArgumentParser(description='Upload files to EGA aspera server')
    parser.add_argument('-f', '--file_name', dest="file_name", help="Input file", required=True)
    parser.add_argument('-o', '--output_directory', dest="output_directory", help="Output directory on Aspera server", required=True)

    results = parser.parse_args()

    try:
        try:

            # Check if ASCP_EGA_USER environment variable exists: ega username
            os.environ['ASCP_EGA_USER']

            # Check if ASPERA_SCP_PASS environment variable exists: ascpera password
            os.environ['ASPERA_SCP_PASS']
        except KeyError:
            raise KeyError(
                "Global Variable: ASCP_EGA_USER and ASPERA_SCP_PASS must exist in the environment.")

        subprocess.call(['ascp',results.file_name,os.environ['ASCP_EGA_USER']+"@fasp.ega.ebi.ac.uk:"+results.output_directory])
    except Exception, err:
        print str(err)
        exit(1)