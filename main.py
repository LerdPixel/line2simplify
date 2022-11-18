import math
import numpy as np

class Order2line:
    factors = []
    factors1 = []
    factors2 = []
    def i1_update(self):
        self.i1 = self.factors[0] + self.factors[2]
    def i2_update(self):
        self.i2 = self.factors[0] * self.factors[2] - self.factors[1] * self.factors[1]
    def i3_update(self):
        b = np.array([[self.factors[0], self.factors[1], self.factors[3]], [self.factors[1], self.factors[2], self.factors[4]], [self.factors[3], self.factors[4], self.factors[5]]])
        self.i3 = np.linalg.det(b)
    def __init__(self, inputFactors):
        if (type(inputFactors) is list):
            if (len(inputFactors) == 6):
                inputFactors[1] /= 2
                inputFactors[3] /= 2
                inputFactors[4] /= 2
                self.factors = inputFactors
        self.i1_update()
        self.i2_update()
        self.i3_update()
        if self.i2 == 0:
            self.type = 'parabola'
        elif self.i2 > 0:
            self.type = 'ellipse'
        else:
            self.type = 'hyperbola'
        if self.type == 'parabola':
            if self.factors[1] == 0:
                self.phi2 = 0
                self.phi = 0
                self.factors1 = self.factors
            else:
                if self.factors[0] == self.factors[2]:
                    self.phi2 = math.pi / 2
                else:
                    self.phi2 = math.atan(2*self.factors[1]/(self.factors[0]-self.factors[2]))
                if self.factors[1] * math.sin(self.phi2) + (self.factors[0] - self.factors[2]) * math.cos(self.phi2) / 2 + (self.factors[0] + self.factors[2]) / 2 != 0:
                    self.phi2 += math.pi
                self.phi = self.phi2 / 2
                self.factors1 = self.rotate(self.phi, self.phi2, self.factors)
            self.factors2 = [0, 0, self.i1, self.factors1[3], 0, self.factors[5] - self.factors1[4]**2 / self.i1]
        else:
            self.factors1 = [self.factors[0], self.factors[1], self.factors[2], 0, 0, self.i3 / self.i2]
            if self.factors[1] == 0:
                self.factors2 = self.factors1
            else:
                if self.factors1[0] == self.factors1[2]:
                    self.phi2 = math.pi / 2
                else:
                    self.phi2 = math.atan(2*self.factors1[1]/(self.factors1[0]-self.factors1[2]))
                self.phi = self.phi2 / 2
                self.factors2 = self.rotate(self.phi, self.phi2, self.factors1)

    def rotate(self, phi, phi2, fac):
        return [fac[1] * math.sin(phi2) + (fac[0] - fac[2]) * math.cos(phi2) / 2 + (fac[0] + fac[2]) / 2, 0, - fac[1] * math.sin(phi2) - (fac[0] - fac[2]) * math.cos(phi2) / 2 + (fac[0] + fac[2]) / 2, fac[3] * math.cos(phi) + fac[4] * math.sin(phi), fac[4] * math.cos(phi) - fac[3] * math.sin(phi), fac[5]]
    def inf_message(self):
        self.intr(self.factors)
        print('I1 = ', self.i1, 'I2 = ', self.i2, 'I3 = ', self.i3)
        print('type = ', self.type)
        self.intr(self.factors1)
        self.intr(self.factors2)
    def intr(self, fac):
        variables = ['x^2', 'x*y', 'y^2', 'x', 'y', '']
        for i in range(6):
            if fac[i] != 0:
                if i in [1, 3, 4]:
                    print(2*fac[i], variables[i], end = ' + ', sep ='')
                else:
                    print(fac[i], variables[i], end = ' + ', sep ='')
        print(' = 0')



a = Order2line([3, 10, 3, -2, -14, -13])
a.inf_message()
