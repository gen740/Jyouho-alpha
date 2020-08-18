from MODEL import *
from mnist import *
from graph import *
import numpy as np

data = []
for i in range(10):
    AI_learning(10, i + 20)
    data.append(save_data())
    np.savetxt(f"data{i + 20}.txt", data)
    print(data)
