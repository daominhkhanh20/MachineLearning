import numpy as np
from numpy.random import rand


class rnn:
    def __init__(self,hiden_unit=100,output_unit=100):
        self.hiden_unit=hiden_unit
        self.output_unit=output_unit
