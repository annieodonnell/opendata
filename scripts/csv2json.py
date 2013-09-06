#!/usr/bin/python

import sys
import getopt
import argparse
import csv
import json

# get command line args
argp = argparse.ArgumentParser(description='script to convert csv file to a json file')
argp.add_argument('-i', '--ifilename', help='input filename', required=True)
argp.add_argument('-o', '--ofilename', help='output filename', default='dump.json')
args = argp.parse_args()

# convert file format...
with open(args.ifilename, 'rU') as ifile:
	ofile = open(args.ofilename,'w') 
	# process input stream and write output stream...
	ofile.write(json.dumps([r for r in csv.DictReader(ifile)], sort_keys=True, indent=4)) 
 	ifile.close()
	ofile.close()