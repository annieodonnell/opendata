#!/usr/bin/python

import sys
import getopt
import argparse
import csv

# define function to extract command line args
argp = argparse.ArgumentParser(description='script to match ISO 3166 country codes')
argp.add_argument('-i', '--ifilename', help='input filename', required=True)
argp.add_argument('-o', '--ofilename', help='output filename', default='dump.csv')
argp.add_argument('-r', '--rfilename', help='reference filename', default='../temp/country-codes-slim.csv')
argp.add_argument('-n', '--countryname', help='country iso-name fieldname', default='country')
argp.add_argument('-a', '--countryalpha3', help='country iso-alpha-3 fieldname', default='isoalpha3')
args = argp.parse_args()


# define function to parse csv file into a dictionary
def loadCsvDict(filename):
	with open(filename, 'rU') as fin:
		dr = csv.DictReader(fin, delimiter=',', quotechar='"')
		header = dr.fieldnames
		data = [r for r in dr]
		return header, data


def writeCsvDict(filename, header, data):
	with open(filename, 'wb') as fou:
		dw = csv.DictWriter(fou, delimiter=',', quotechar='"', fieldnames=header)
		dw.writeheader()
		dw.writerows(data)


# define main function to search iso dictionary 
def main():
	# load iso & src data
	isohdr, isodata = loadCsvDict(args.rfilename)
	srchdr, srcdata = loadCsvDict(args.ifilename)
	score = 0;

	# check if isoalpha3 field exists in source header
	if args.countryalpha3 not in srchdr:
		srchdr.append(args.countryalpha3)

	# parse source data	
	for dict in srcdata:
		
		# lookup country name
		result = filter(lambda q: q['short_name_en'] == dict[args.countryname].upper(), isodata)

		# bind result
		if (len(result) == 1):
			score += 1
			dict[args.countryalpha3] = result[0]['iso3166-1-alpha-3']
		else:
			dict[args.countryalpha3] = '???'

	# write cleaned data to file
	writeCsvDict('dump.csv', srchdr, srcdata);

	print('search complete >> found = ' + str(score) + '/' + str(len(srcdata)))
	

# exectute main method
if  __name__ =='__main__':main()