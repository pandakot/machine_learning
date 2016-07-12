import argparse
import csv
from functions import *
from collections import defaultdict
from random import shuffle
import os


params_file1 = 'params_train.txt'
params_file2 = 'params_validate.txt'
params_file3 = 'params_test.txt'


parser = argparse.ArgumentParser()
parser.add_argument('--dataset', required=True)
parser.add_argument('--model-folder', dest='model_folder', required=True)


def main():
    args = parser.parse_args()

    if not os.path.exists(args.model_folder):
        os.makedirs(args.model_folder)

    print('Generating dict')
    with open(args.dataset) as csvfile:
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

        popular_words = _get_popular_words(word_counts, 100)
        _save_dict_to_file(os.path.join(args.model_folder, 'dict.txt'), popular_words)

    print('Generating parameters')
    with open(args.dataset) as csvfile:
        lines = []
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

        with open(os.path.join(args.model_folder, params_file1), 'w') as fp:
            for i in range(0, count_train - 1):
                fp.write(lines[i])

        with open(os.path.join(args.model_folder, params_file2), 'w') as fp:
            for i in range(count_train, count_train + count_validate - 1):
                fp.write(lines[i])

        with open(os.path.join(args.model_folder, params_file3), 'w') as fp:
            for i in range((count_validate + count_train), len(lines) - 1):
                fp.write(lines[i])


def _get_popular_words(wordDict, threshold=4):
    print(len(wordDict))

    dictList = []
    for word in wordDict:
        if len(word) > 1 and wordDict[word] > threshold:
            dictList.append(word)

    return sorted(dictList)


def _save_dict_to_file(file_name, word_dict):
    with open(file_name, 'w') as f:

        i = 1
        for word in word_dict:
            f.write(str(i) + '\t' + word + '\n')
            i += 1


if __name__ == '__main__':
    main()
