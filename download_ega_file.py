#!/usr/bin/env python

"""
This file download a from EGA server using aspera.
For this script to works, the files under aspera have to be set-up in the following tree structure.

data
|___ {project_name}
           |____ {EGA_FILE_ACCESSION}.ext

Example:
	$ python download_ega_file.py -p {PROJECT} -f {FILE_ACCESSION} -o {OUTPUT_FILE}

Attributes:
    project_name (String): Name of the ICGC project
"""

import argparse
import subprocess
import random, string
import os
import shutil

def main():
	#Parsing of the input parameters using argparse
	parser = argparse.ArgumentParser(description='Download files from EGA aspera server')
	parser.add_argument('-p', '--project_name', dest="project_name", help="Name of the ICGC project", required=True)
	parser.add_argument('-f', '--file_name', dest="file_name", help="EGA file name", required=True)
	parser.add_argument('-o', '--output', dest='output', help="Output file name", required=True)

	results = parser.parse_args()

	# Generate random file name to output name of file to be downloaded
	file_list = randomword(60)+".txt"

	try:
		try:
			# Check if ASCP_EGA_HOST environment variable exists: ega host
			os.environ['ASCP_EGA_HOST']

			# Check if ASCP_EGA_USER environment variable exists: ega username
			os.environ['ASCP_EGA_USER']

			# Check if ASPERA_SCP_PASS environment variable exists: ascpera password
			os.environ['ASPERA_SCP_PASS']
		except KeyError:
			raise KeyError("Global Variable: ASCP_EGA_HOST, ASCP_EGA_USER and ASPERA_SCP_PASS must exist in the environment.")

		# Raise an error if the output file exists
		if os.path.isfile(results.output):
			raise ValueError("Output file already exists")

		# Write the file to be downloaded to the temporary file
		with open(file_list, 'w') as f:
			f.write(os.path.join('data',results.project_name,results.file_name))
			f.write('\n')

		# Download process
		subprocess.call(['ascp','-k','1','-QTl','100m','--file-list='+file_list,'--partial-file-suffix=PART','--ignore-host-key','--mode=recv','--host='+os.environ['ASCP_EGA_HOST'],'--user='+os.environ['ASCP_EGA_USER'],'.'])

		shutil.move(os.path.basename(results.file_name), results.output)

		# Deletion of temporary elements
		os.remove(file_list)
	except Exception, err:
		print str(err)
		if os.path.isfile(file_list):
			os.remove(file_list)
		exit(1)



def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

if __name__ == "__main__":
    main()
