from nltk.tokenize import RegexpTokenizer

import nltk, re


def build_params(filename):
    print('build_params')
    fp = open(filename, 'r')

    Xbig = []
    y = []

    i = 0
    for line in fp.readlines():

        x = []
        line = line.split(' ')
        j = 1
        line_len = len(line)
        for p in line :

            if j < line_len:
                x.append(int(p))
            else:
                y.append(int(p.strip('\n')))
            j += 1
        Xbig.append(x)
        i += 1

    print(i)
    fp.close()
    return {'x': Xbig, 'y': y}


_stemm_tokenizer = RegexpTokenizer(r'\w+')
def stemm(text):
    # removing all numbers
    text = re.sub(r'\d+', 'number', text)
    text = text.lower()

    tokens = _stemm_tokenizer.tokenize(text)
    russian_stemmer = nltk.stem.snowball.RussianStemmer()

    # TODO: should we remove 2 letter words?

    return [russian_stemmer.stem(t) for t in tokens]


def load_dict(filename):
    wordDict = {}
    dictFile = open(filename, 'r')

    wd = []
    for line in dictFile.readlines() :
        line = line.split('\t')
        wordDict[line[1].strip('\n')] = line[0]
        wd.append(line[1].strip('\n'))

    dictFile.close()
    return wd




