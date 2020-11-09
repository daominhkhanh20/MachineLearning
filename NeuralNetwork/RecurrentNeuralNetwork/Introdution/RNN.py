import numpy as np
from numpy.random import randn


class rnn:
    def __init__(self,input_size=100,hiden_size=100,output_size):
        self.Wxh=randn(hiden_size,input_size)/1000
        self.Whh=randn(hiden_size,hiden_size)/1000
        self.Why=randn(output_size,hiden_size)/1000
        self.bh=np.zeros((hiden_size,1))
        self.by=np.zeros((output_size,1))

    def feedforward(self,inputs):
        h=np.zeros((self.Whh.shape[0],1))
        self.h_list={0:h}

        for i,x in enumerate(inputs):
            h=np.tanh(self.Wxh.dot(x)+self.Whh.dot(h)+self.bh)
            self.h_list[i+1]=h #update the new state from the previous state

        y=self.Why.dot(h)+self.by
        return y,h