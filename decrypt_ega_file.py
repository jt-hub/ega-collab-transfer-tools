#!/usr/bin/env python

import argparse
import os
import subprocess

def main():
	parser = argparse.ArgumentParser(description='Decrypt EGA encrypted file')
	parser.add_argument('-i', '--input', dest="input", help="File to decrypt", required=True)
	parser.add_argument('-o', '--output', dest="output", help="Output file", required=True)

	results = parser.parse_args()

	try:
		try:
			os.environ['EGA_DCK_KEY']
		except KeyError:
			raise KeyError("Global Variable (Ega decryption key): EGA_DCK_KEY must exist as an environment variable")

		if not os.path.isfile(results.input):
			raise ValueError("Input file does not exists: "+results.input)

		if os.path.isfile(results.output):
			raise ValueError("Output file already exists: "+results.output)

		subprocess.call(['openssl','enc','-aes-256-cbc','-d','-in',results.input,'-out',results.output,'-k',os.environ['EGA_DCK_KEY']])
	except Exception, err:
		print err
		exit(1)

if __name__ == "__main__":
	main()
