from MODEL import *
from mnist import *
from graph import *
import numpy as np

data = []
for i in range(10):
    x = i + 32
    AI_learning(10 * x, 2)
    data.append(save_data())
    np.savetxt(f"./DATA/data{x}.txt", data)
    print(data)
