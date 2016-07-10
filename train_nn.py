from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer
import cPickle as pickle
from math import sqrt

import numpy as np
from functions import *

from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection, RecurrentNetwork
from pybrain.tools.shortcuts import buildNetwork

########################################
hidden_size = 50
epochs = 10
params_len = 792

trainParams = build_params('model/params_train.txt')

y = []
for y1 in trainParams['y']:
    y.append(example_result(y1))

print len(trainParams['x'])
print len(y)

# TODO: fix the number of pictures
ds = SupervisedDataSet( params_len, 601 )
ds.setField( 'input', trainParams['x'] )
ds.setField( 'target', y )


# init and train



net = FeedForwardNetwork()

""" Next, we're constructing the input, hidden and output layers. """

inLayer = LinearLayer(params_len)
hiddenLayer = SigmoidLayer(50)
hiddenLayer1 = SigmoidLayer(50)
outLayer = LinearLayer(601)

""" (Note that we could also have used a hidden layer of type TanhLayer, LinearLayer, etc.)
Let's add them to the network: """

net.addInputModule(inLayer)
net.addModule(hiddenLayer)
net.addModule(hiddenLayer1)
net.addOutputModule(outLayer)

""" We still need to explicitly determine how they should be connected. For this we use the most
common connection type, which produces a full connectivity between two layers (or Modules, in general):
the 'FullConnection'. """

in2hidden = FullConnection(inLayer, hiddenLayer)
hidden2hidden = FullConnection(hiddenLayer, hiddenLayer1)
hidden2out = FullConnection(hiddenLayer1, outLayer)

net.addConnection(in2hidden)
net.addConnection(hidden2hidden)
net.addConnection(hidden2out)

""" All the elements are in place now, so we can do the final step that makes our MLP usable,
which is to call the 'sortModules()' method. """

net.sortModules()

#net = buildNetwork( params_len, hidden_size, 601, bias = True )
trainer = BackpropTrainer( net, ds )

print "training for {} epochs...".format( epochs )

#trainer.trainUntilConvergence(verbose=True)

for i in range( epochs ):
    mse = trainer.train()
    rmse = sqrt( mse )
    print "training RMSE, epoch {}: {}".format( i + 1, rmse )

pickle.dump( net, open('model/model_nn.pkl', 'wb' ))





