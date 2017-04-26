#This script takes in a directory containing protein reports from peptide shaker and determine number of confident proteins identified.

'''
Usage: protein_report_parser_confident.py protein_report_file_directory
'''

import sys, glob

folder = sys.argv[1]

reports = glob.glob(folder + '*Protein_Report.txt')

confident_proteins = 0

for report in reports:
	with open(report,'r') as report_file:
		next(report_file)
		for line in report_file:
			line_split = line.strip().split('\t') #split tab delim line
			if line_split[-1] == 'Confident': #check if protein is confident
				confident_proteins += 1

print('%i Confident Proteins identified' % confident_proteins)