import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from ast import literal_eval

data = np.loadtxt("./TBP_sim/build/data_for_learning/forward_step_data.csv")
print(data.shape)

data_shape=data.shape

mask = []
for i in range(int(data_shape[1]/4)):
    mask = np.append(mask,np.array([True,True,False,False]))
print(mask)
reshaped_data = data[:,np.array(mask,dtype=bool)]

print(data)
print(reshaped_data.shape)

star1 = []
star2 = []
star3 = []

for i in range(int(data_shape[1]/12)):
    star1 = np.append(star1,np.array([True,True,False,False,False,False]))
    star2 = np.append(star2,np.array([False,False,True,True,False,False]))
    star3 = np.append(star3,np.array([False,False,False,False,True,True]))

star1 = reshaped_data[8,np.array(star1,dtype=bool)]
star2 = reshaped_data[8,np.array(star2,dtype=bool)]
star3 = reshaped_data[8,np.array(star3,dtype=bool)]


star1_data = star1.reshape(int(data_shape[1]/12),2)
star2_data = star2.reshape(int(data_shape[1]/12),2)
star3_data = star3.reshape(int(data_shape[1]/12),2)

fig, ax = plt.subplots()

ax.plot(star1_data[:,0],star1_data[:,1],".")
ax.plot(star2_data[:,0],star2_data[:,1],".")
ax.plot(star3_data[:,0],star3_data[:,1],".")

fig.show()
plt.show()
