import math
class TriangleArea:
    def __init__(self, a, c, beta):
        self.a = a
        self.c = c
        self.beta = beta
    def area(self):
        if (self.beta < 180 and self.beta > 0):
            vc = math.sin(math.radians(self.beta)) * self.a
            S = (self.c * vc)/2
            return S
