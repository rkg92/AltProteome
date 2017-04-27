#This script takes in a directory containing peptide reports from peptide shaker and determine number of confident, unique proteins identified.
#It outputs a file that shows the protein by accession and the number of times it was seen confidently.

'''
Usage: peptide_report_parser_confident.py protein_report_file_directory
'''

import sys, glob

folder = sys.argv[1]

reports = glob.glob(folder + '*Peptide_Report.txt')

confident_proteins = 0
proteins_set = {}

for report in reports:
	with open(report,'r') as report_file:
		next(report_file)
		for line in report_file:
			line_split = line.strip().split('\t') #split tab delim line
			if line_split[-1] == 'Confident': #check if protein is confident
				if not line_split[5] in proteins_set:
					proteins_set[line_split[5]] = 1
					confident_proteins += 1
				else:
					proteins_set[line_split[5]] += 1



print('%i Confident Sequences identified' % confident_proteins)

with open(folder[:-1] + '_unique_confident_peptide.txt', 'w') as out_file:
	out_file.write('sequence\tcount\n')
	for key in proteins_set:
		out_file.write('%s\t%i\n' % (key, proteins_set[key]))