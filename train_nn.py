from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer
import cPickle as pickle
from math import sqrt

import numpy as np
from functions import *

########################################
hidden_size = 50
epochs = 2
params_len = 236

trainParams = build_params('model/params_train.txt')

y = []
for y1 in trainParams['y']:
	y.append(example_result(y1))

print len(trainParams['x'])
print len(y)

ds = SupervisedDataSet( params_len, 601 )

ds.setField( 'input', trainParams['x'] )
ds.setField( 'target', y )


# init and train


net = buildNetwork( params_len, hidden_size, 601, bias = True )
trainer = BackpropTrainer( net, ds )

print "training for {} epochs...".format( epochs )

#trainer.trainUntilConvergence(verbose=True)

for i in range( epochs ):
	mse = trainer.train()
	rmse = sqrt( mse )
	print "training RMSE, epoch {}: {}".format( i + 1, rmse )
	
pickle.dump( net, open('model/model_nn.pkl', 'wb' ))





