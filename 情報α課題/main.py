from MODEL import *
from mnist import *
from graph import *
import numpy as np

data = []
for i in range(2):
    AI_learning(15, i + 1)
    data.append(save_data())
np.savetxt("data.txt", data)
print(data)
make_graph("fig1")
