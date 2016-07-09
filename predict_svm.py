# -*- coding: utf-8 -*-

from sklearn import svm
from sklearn.externals import joblib
from functions import *

clf = joblib.load('model/model_svc.pkl') 


text = 'нельзя просто взять и вышел 10'

stemmed = stemm(text, '', '')
stemmed = stemmed.split(' ')

x = []

wordDict = load_dict('dict.txt')
for word in wordDict :	
	x.append(stemmed.count(word))

print x

pred = clf.predict([x])

print pred
