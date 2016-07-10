from nltk.tokenize import RegexpTokenizer

import nltk, re, pprint
from nltk.corpus import PlaintextCorpusReader
from io import StringIO
import sys


def upgrade_keyword(keyword):
    new_keyword = ''
    corpus_root = './'
    newcorpus = PlaintextCorpusReader(corpus_root, '.*')
    words = newcorpus.words('corpus.txt')
    text = nltk.Text(words)

    kwords = keyword.split(' ')
    for kw in kwords:
        new_keyword += get_similar(text, kw) + ' '

    return new_keyword

def get_similar(text, word):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO.StringIO()

    #text.common_contexts([u'был'], 10)
    #text.concordance(u'был')
    text.similar(word)
    x = mystdout.getvalue()
    sys.stdout = old_stdout
    mystdout.close()

    return x.strip()

####################################
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


##################################
def dict_process(wordDict):
    print(len(wordDict))

    dictList = []
    for word in wordDict:
        if len(word)>1 and wordDict[word] > 100 :
            dictList.append(word)

    return sorted(dictList)



#################################
def save_dict_to_file(wordDict):
    print(len(wordDict))

    file_name = 'dict.txt'
    f = open(file_name, 'w')

    i = 1
    for word in wordDict:
        f.write( str(i) + '\t' + word + '\n')
        i += 1

    f.close()

#################################
_stemm_tokenizer = RegexpTokenizer(r'\w+')
def stemm(text):
    # removing all numbers
    text = re.sub(r'\d+', 'number', text)
    text = text.lower()

    tokens = _stemm_tokenizer.tokenize(text)
    russian_stemmer = nltk.stem.snowball.RussianStemmer()

    # TODO: should we remove 2 letter words?

    return [russian_stemmer.stem(t) for t in tokens]


###############################
def example_result(text_result, output_layer_num):
    count_images = [0] * output_layer_num

    count = 0
    for i in count_images:
        if count_images[count] == (int(text_result)-1):
            # print(str(count) + ': !!!!!!!!!!!!!!')
            count_images[count] = 1
        count += 1

    return count_images

##################################
def show_relation(relation_num):
    relation = 'Relation unclassified'

    if relation_num == 1 :
        relation = 'No relation exists between the companies'
    elif relation_num == 2 :
        relation = 'Some direct relation exists between the companies, but is not a valid supplier-customer relation'
    elif relation_num == 3 :
        relation = 'B supplies A'
    elif relation_num == 4 :
        relation = 'A supplies B'

    return relation

############################
def load_dict(filename) :
    wordDict = {};
    dictFile = open(filename, 'r')

    wd = []
    for line in dictFile.readlines() :
        line = line.split('\t')
        wordDict[line[1].strip('\n')] = line[0]
        wd.append(line[1].strip('\n'))

    dictFile.close()
    return wd



