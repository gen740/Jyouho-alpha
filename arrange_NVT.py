import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from ast import literal_eval

initial = np.loadtxt("./TBP_sim/build/data_for_learning/initial_value.csv")
data = np.loadtxt("./TBP_sim/build/data_for_learning/forward_dt_data.csv")
print("data_shape = ", data.shape)

data_shape=data.shape

mask = []
for i in range(int(data_shape[1]/4)):
    mask = np.append(mask,np.array([True,True,False,False]))
reshaped_data = data[:,np.array(mask,dtype=bool)]

Result = np.max(np.absolute(reshaped_data),1)

counter = 0
mask = []
for i in Result:
    if i > 2.0:
        mask.append(False)
    else:
        mask.append(True)
    counter += 1

reshaped_data = reshaped_data[mask,:]
initial = initial[mask,:]
data_shape=reshaped_data.shape

print("initial_shape = ", initial.shape, \
        ": reshaped_data = ", reshaped_data.shape)

fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()

ax.plot(Result)
Result = np.max(np.absolute(reshaped_data),1)
ax2.plot(Result)

plt.show()

t = initial[:,0]
x_2 = initial[:,7:9]

initial = np.concatenate([t.reshape(data_shape[0],1),x_2],1)
print("Re_initial = ", initial.shape)

star1 = []
star2 = []

for i in range(int(data_shape[1]/6)):
    star1 = np.append(star1,np.array([True,True,False,False,False,False]))
    star2 = np.append(star2,np.array([False,False,True,True,False,False]))

star1 = reshaped_data[:,np.array(star1,dtype=bool)]
star2 = reshaped_data[:,np.array(star2,dtype=bool)]

reshaped_data = np.concatenate([star1,star2],1)

print("Re_reshaped_data = ", reshaped_data.shape)

np.savetxt("./TBP_sim/build/data_for_learning/Re_initial_value.csv", \
        initial)
np.savetxt("./TBP_sim/build/data_for_learning/Re_forward_step_data.csv", \
        reshaped_data)
