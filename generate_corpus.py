from functions import *
import csv

csv_file = 'dataset.csv';
corp_file = 'corpus.txt'

with open(csv_file) as csvfile:
	reader = csv.DictReader(csvfile)
	
	fp = open(corp_file , 'w')
	i = 0
	for row in reader:
		fp.write(row['title']+' ')

	fp.close()
