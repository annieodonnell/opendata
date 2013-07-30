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

# define function to parse strings to numbers
# not working! - add param 'cls=ParseString' to the json.dump call
class ParseString(json.JSONEncoder):
	def default(self, obj):
	    try:
	    	return float(obj)
	    except Exception:
	        return obj

# convert file format...
with open(args.ifilename, 'rU') as ifile:
	print "Opening CSV file: ", args.ifilename 
	reader = csv.DictReader(ifile)
	print "Saving JSON to file: ", args.ofilename
	ofile = open(args.ofilename,'w') 
	ofile.write(json.dumps([r for r in reader], sort_keys=True, indent=4)) 
 	ifile.close()
	ofile.close()