import pickle as pickle
import sys

from functions import *


net = pickle.load(open('model/model_nn.pkl', 'rb'))
wordDict = load_dict('dict.txt')


def predict(text):
    stemmed = stemm(text)

    x = []

    for word in wordDict:
        x.append(stemmed.count(word))

    pred = net.activate(x)

    res = max(enumerate(pred), key=lambda x: x[1])[0] + 1
    return res


if __name__ == '__main__':
    text = sys.argv[1]
    print(predict(text))
