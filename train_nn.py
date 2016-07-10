from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer
import pickle as pickle
from math import sqrt

import numpy as np
from functions import *

from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection, RecurrentNetwork
from pybrain.tools.shortcuts import buildNetwork


def _build_params(filename):
    print('build_params')
    with open(filename, 'r') as fp:

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

    return {'x': Xbig, 'y': y}


def main():
    hidden_size = 50
    epochs = 10

    trainParams = _build_params('model/params_train.txt')

    # get params len from the X vector
    params_len = len(trainParams['x'][0])
    output_layer_num = 601

    y = []

    for y_val in trainParams['y']:
        y_vec = [0] * output_layer_num
        y_vec[y_val - 1] = 1
        y.append(y_vec)

    print(len(trainParams['x']))
    print(len(y))

    # TODO: fix the number of pictures
    ds = SupervisedDataSet(params_len, output_layer_num)
    ds.setField('input', trainParams['x'])
    ds.setField('target', y)

    # init and train
    net = FeedForwardNetwork()

    """ Next, we're constructing the input, hidden and output layers. """
    inLayer = LinearLayer(params_len)
    hiddenLayer = SigmoidLayer(50)
    hiddenLayer1 = SigmoidLayer(50)
    outLayer = LinearLayer(output_layer_num)

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
    trainer = BackpropTrainer(net, ds)

    print("training for {} epochs...".format(epochs))

    #trainer.trainUntilConvergence(verbose=True)

    for i in range(epochs):
        mse = trainer.train()
        rmse = sqrt(mse)
        print("training RMSE, epoch {}: {}".format(i + 1, rmse))

    pickle.dump(net, open('model/model_nn.pkl', 'wb'))


if __name__ == '__main__':
    main()
