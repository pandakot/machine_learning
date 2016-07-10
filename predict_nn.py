import pickle as pickle
import sys

from functions import *


net = pickle.load(open('model/model_nn.pkl', 'rb'))

text = sys.argv[1]
# text = upgrade_keyword(text0) + text0
# text = text.encode('utf-8')

stemmed = stemm(text)

x = []


wordDict = load_dict('dict.txt')
for word in wordDict:
    x.append(stemmed.count(word))

pred = net.activate(x)

print(pred)

res = max(enumerate(pred), key=lambda x: x[1])[0] + 1

print(res)



