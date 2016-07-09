from sklearn import svm
from sklearn.externals import joblib
import numpy as np
from functions import *
from sklearn import linear_model, datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, Perceptron
########################################

trainParams = build_params('model/params_train.txt')
validateParams = build_params('model/params_validate.txt')


clf = svm.SVC(C=100, gamma=0.01)
print clf.fit(np.array(trainParams['x']), np.array(trainParams['y']))
print clf.score(np.array(validateParams['x']), np.array(validateParams['y']))  

#C = [1, 5, 15, 20, 30, 100, 1000]
#gamma = [0.001, 0.01, 0.1, 1]
#for c in C:
#	for g in gamma:
#		print '\nC: %f, gamma: %f' % (c, g)
        #decision_function_shape='ovo
#		clf = svm.LinearSVC(C=c)#, gamma=g, kernel='rbf')
#		print clf.fit(np.array(trainParams['x']), np.array(trainParams['y']))  
#		print clf.score(np.array(validateParams['x']), np.array(validateParams['y']))  

joblib.dump(clf, 'model/model_svc.pkl')  
