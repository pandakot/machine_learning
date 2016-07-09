from functions import *
from random import shuffle
import csv

csv_file = 'dataset.csv'

params_file1 = 'model/params_train.txt'
params_file2 = 'model/params_validate.txt'
params_file3 = 'model/params_test.txt'


lines = []
with open(csv_file) as csvfile:
    reader = csv.DictReader(csvfile)
    wordDict = load_dict('dict.txt')


    i = 0
    
    for row in reader:
        stemmed = stemm(row['title'], '', '')

        stemmed = stemmed.split(' ')

        line = ''
        for word in wordDict :
            line += str(stemmed.count(word)) + ' '

        line += row['img_id'] + '\n'
        lines.append(line)


        if i % 100 == 0:
            print i

        i += 1

    shuffle(lines)

    count_train = 95 * len(lines) / 100
    count_validate = 5 * len(lines) / 100

    print count_train
    print count_validate
    print len(lines)

    fp = open(params_file1 , 'w')
    for i in range(0, count_train - 1):
        fp.write(lines[i])
    fp.close()

    fp = open(params_file2 , 'w')
    for i in range(count_train, count_train + count_validate - 1):
        fp.write(lines[i])
    fp.close()

    fp = open(params_file3 , 'w')
    for i in range((count_validate + count_train), len(lines) - 1):
        fp.write(lines[i])
    fp.close()
