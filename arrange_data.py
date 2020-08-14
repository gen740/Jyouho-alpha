import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from ast import literal_eval

initial = np.loadtxt("./TBP_sim/build/data_for_learning/initial_value.csv")
data = np.loadtxt("./TBP_sim/build/data_for_learning/forward_step_data.csv")
print(data.shape)

data_shape=data.shape

mask = []
for i in range(int(data_shape[1]/4)):
    mask = np.append(mask,np.array([True,True,False,False]))
reshaped_data = data[:,np.array(mask,dtype=bool)]

Result = np.sum(np.absolute(reshaped_data),1)

counter = 0
mask = []
for i in Result:
    if i > 600:
        mask.append(False)
    else:
        mask.append(True)
    counter += 1

reshaped_data = reshaped_data[mask,:]
initial = initial[mask,:]

print(initial.shape, reshaped_data.shape)

np.savetxt("./TBP_sim/build/data_for_learning/Re_initial_value.csv",initial)
np.savetxt("./TBP_sim/build/data_for_learning/Re_forward_step_data.csv",reshaped_data)

"""
fig, ax = plt.subplots()

ax.plot(Result)

#fig.show()
plt.show()
"""
