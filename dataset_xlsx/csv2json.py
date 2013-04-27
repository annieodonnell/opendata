#!/usr/bin/python

import sys
import getopt
import argparse
import csv
import json

# get command line args
parser = argparse.ArgumentParser(description='script to convert csv file to a json file')
parser.add_argument('-i', '--ifilename', help='input filename', required=True)
parser.add_argument('-o', '--ofilename', help='output filename', default='dump.json')
args = parser.parse_args()

# convert file format...
with open(args.ifilename, 'rU') as ifile:
	print "Opening CSV file: ", args.ifilename 
	reader = csv.DictReader(ifile)
	print "Saving JSON to file: ", args.ofilename
	ofile = open(args.ofilename,'w') 
	ofile.write(json.dumps([r for r in reader])) 
 	ifile.close()
	ofile.close()