import os
import csv
import json

cfilename = 'scogov_simd.csv'
jfilename = 'scogov_simd.json'

with open(cfilename, 'rU') as csvfile:
	print "Opening CSV file: ", cfilename 
	reader = csv.DictReader(csvfile)
	print "Saving JSON to file: ", jfilename
	jsofile = open(jfilename,'w') 
	jsofile.write(json.dumps([r for r in reader])) 
 	csvfile.close()
	jsofile.close()
