import csv
from functions import *
from collections import defaultdict
from random import shuffle


csv_file = 'dataset.csv'

params_file1 = 'model/params_train.txt'
params_file2 = 'model/params_validate.txt'
params_file3 = 'model/params_test.txt'


def _get_popular_words(wordDict, threshold=100):
    print(len(wordDict))

    dictList = []
    for word in wordDict:
        if len(word) > 1 and wordDict[word] > threshold:
            dictList.append(word)

    return sorted(dictList)


def main():
    print('Generating dict')
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        word_counts = defaultdict(int)

        i = 0
        for row in reader:
            stemmed = stemm(row['title'])

            for word in stemmed:
                word_counts[word] += 1

            if i % 100 == 0:
                print(i)

            i += 1

        popular_words = _get_popular_words(word_counts)
        save_dict_to_file(popular_words)

    print('Generating parameters')
    lines = []
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)

        i = 0
        for row in reader:
            stemmed = stemm(row['title'])

            line = ' '.join(str(stemmed.count(word)) for word in popular_words)

            line += ' '
            line += row['img_id'] + '\n'
            lines.append(line)

            if i % 100 == 0:
                print(i)

            i += 1

        shuffle(lines)

        count_train = 95 * len(lines) // 100
        count_validate = 5 * len(lines) // 100

        print(count_train)
        print(count_validate)
        print(len(lines))

        fp = open(params_file1, 'w')
        for i in range(0, count_train - 1):
            fp.write(lines[i])
        fp.close()

        fp = open(params_file2, 'w')
        for i in range(count_train, count_train + count_validate - 1):
            fp.write(lines[i])
        fp.close()

        fp = open(params_file3, 'w')
        for i in range((count_validate + count_train), len(lines) - 1):
            fp.write(lines[i])
        fp.close()


if __name__ == '__main__':
    main()
