# -*- coding: utf-8 -*-

import numpy as np
import cPickle as pickle

from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE

from functions import *

net = pickle.load( open( 'model/model_nn.pkl', 'rb' ))

text0 = u'белка и хуй'
text = upgrade_keyword(text0) + text0
text = text.encode('utf-8') 

stemmed = stemm(text, '', '')
stemmed = stemmed.split(' ')

x = []

wordDict = load_dict('dict.txt')
for word in wordDict :	
    x.append(stemmed.count(word))

pred = net.activate(x)
res = max(enumerate(pred),key=lambda x: x[1])[0] + 1

print res

