import csv
from functions import *
from collections import defaultdict


csv_file = 'dataset.csv';


def main():
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        word_counts = defaultdict(int)

        i = 0
        for row in reader:
            stemmed = stemm(row['title'], '', '')
            #print stemmed + '\n'

            for word in stemmed:
                word_counts[word] += 1

            if i % 100 == 0:
                print i

            i += 1

        words = dict_process(word_counts)
        save_dict_to_file(words)


if __name__ == '__main__':
    main()