from MODEL import *
from mnist import *
from graph import *
import numpy as np

data = []
for i in range(20):
    x = i + 20
    AI_learning(x * 5, 3)
    data.append(save_data())
    np.savetxt(f"./DATA/data{x + 22}.txt", data)
    print(data)
