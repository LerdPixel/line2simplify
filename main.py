import math
import numpy as np

class Order2line:
    def __init__(self, inputFactors):
        if (type(inputFactors) is list):
            if (len(inputFactors) == 6):
                inputFactors[1] /= 2
                inputFactors[3] /= 2
                inputFactors[4] /= 2
                self.factors = inputFactors
        self.i1 = inputFactors[0] + inputFactors[2]
