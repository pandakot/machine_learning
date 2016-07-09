#from cement.core.foundation import CementApp
#app = CementApp('process_ds')
#app.setup()
#app.run()

from functions import *
import csv

csv_file = 'dataset.csv';

with open(csv_file) as csvfile:
	reader = csv.DictReader(csvfile)
	wordDict = {}

	i = 0
	for row in reader:
		stemmed = stemm(row['title'], '', '')
		#print stemmed + '\n'

		wordDict = dict_stemmed(stemmed, wordDict)

		if i % 100 == 0:
			print i
	
		i += 1		

 	words = dict_process(wordDict)
	save_dict_to_file(words)
