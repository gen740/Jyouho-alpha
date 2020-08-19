from MODEL import *
from mnist import *
from graph import *
import numpy as np

data = []
for i in range(50):
    x = i + 1 
    AI_learning(x * 10, 2)
    data.append(save_data())
    np.savetxt(f"./DATA/data{x}.txt", data)
    print(data)
