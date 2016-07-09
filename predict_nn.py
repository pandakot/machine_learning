# -*- coding: utf-8 -*-

import numpy as np
import cPickle as pickle

from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE

from functions import *

net = pickle.load( open( 'model/model_nn.pkl', 'rb' ))

text = 'нельзя просто взять нарисовать хуй'

stemmed = stemm(text, '', '')
stemmed = stemmed.split(' ')

x = []

wordDict = load_dict('dict.txt')
for word in wordDict :	
	x.append(stemmed.count(word))

print x

pred = net.activate(x)
res = max(enumerate(pred),key=lambda x: x[1])[0] + 1

print res

