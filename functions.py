from nltk.tokenize import RegexpTokenizer
import nltk, re

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

    text = text.lower()
    text = _replace_important(text)
    # removing all numbers
    text = re.sub(r'\d+', 'number', text)


    tokens = _stemm_tokenizer.tokenize(text)
    russian_stemmer = nltk.stem.snowball.RussianStemmer()

    # TODO: should we remove 2 letter words?

    return [russian_stemmer.stem(t) for t in tokens]

_important_words = [
    (':*', ' KISS '),
    (';*', ' KISS '),
    ('=*', ' KISS '),
    ('!?', ' EXCLRIDDL '),
    ('?!', ' EXCLRIDDL '),
    ('!', ' EXCLAMATION '),
    ('?', ' QUESTION '),
    (':-)', ' SMILE '),
    ('=)', ' SMILE '),
    ('))', ' SMILE '),
    ('((', ' ANTISMILE '),
    (':-(', ' ANTISMILE '),
    (';-(', ' ANTISMILE '),
    (';-)', ' WINK '),
    (':)', ' SMILE '),
    (';)', ' WINK '),
    (':3', ' CATFACE '),
    ('^_^', ' CATFACE '),
    (':d', ' BIGSMILE '),
    (';d', ' BIGSMILE '),
    (':-d', ' BIGSMILE '),
    ('..', ' ETCR '),
    ('яя', ' GREATI '),
    ('ла-ла', ' SINGSONG '),
    ('+100500', ' PLUSBIGNUMBER '),
    ('100500', ' BIGNUMBER '),
    ('$', ' DOLLAR '),
    ('ну-ну', ' SARCASM '),
    ('ммм', ' DREAMING '),
    ('ааа', ' SCARY '),
    ('(c)', ' COPYRIGHT '),
    ('%', ' PERCENT ')
]
def _replace_important(text):
    for (word, replacement) in _important_words:
        text = text.replace(word, replacement)
    return text

def load_dict(filename):
    dictFile = open(filename, 'r')

    wd = []
    for line in dictFile.readlines() :
        line = line.split('\t')
        wd.append(line[1].strip('\n'))

    dictFile.close()
    return wd




