import numpy as np


class test:
    def __init__(self):
        self.random = np.random.random()
    def rand(self):
        b = self.random
        return b


a = test()

for i in range(10):
    print(a.rand())
