import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from ast import literal_eval

initial = np.loadtxt("./TBP_sim/build/data_for_learning/initial_value.csv")
data = np.loadtxt("./TBP_sim/build/data_for_learning/forward_step_data.csv")
print("data_shape = ", data.shape)

data_shape=data.shape

mask = []
for i in range(int(data_shape[1]/4)):
    mask = np.append(mask,np.array([True,True,False,False]))
reshaped_data = data[:,np.array(mask,dtype=bool)]

Result = np.sum(np.absolute(reshaped_data),1)

counter = 0
mask = []
for i in Result:
    if i > data_shape[1]:
        mask.append(False)
    else:
        mask.append(True)
    counter += 1

reshaped_data = reshaped_data[mask,:]
initial = initial[mask,:]

print("initial_shape = ", initial.shape, \
        ": reshaped_data = ", reshaped_data.shape)

fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()

ax.plot(Result)
Result = np.sum(np.absolute(reshaped_data),1)
ax2.plot(Result)

plt.show()

x_2 = initial[:,5:10] - initial[:,0:5]
x_3 = initial[:,10:15] - initial[:,0:5]

initial = np.concatenate([x_2[:,1:5],x_3[:,1:5]],1)
print("Re_initial = ", initial.shape)

data_shape=reshaped_data.shape
star1 = []
star2 = []
star3 = []

for i in range(int(data_shape[1]/6)):
    star1 = np.append(star1,np.array([True,True,False,False,False,False]))
    star2 = np.append(star2,np.array([False,False,True,True,False,False]))
    star3 = np.append(star3,np.array([False,False,False,False,True,True]))

star1 = reshaped_data[:,np.array(star1,dtype=bool)]
star2 = reshaped_data[:,np.array(star2,dtype=bool)]
star3 = reshaped_data[:,np.array(star3,dtype=bool)]

star2 = (star2 - star1)
star2_shape = star2.shape
star3 = (star3 - star1)
star3_shape = star3.shape

print(star2_shape[0] * star2_shape[1])

star2 = star2.reshape(star2_shape[0], int(star2_shape[1] / 2), 2)
star3 = star3.reshape(star3_shape[0], int(star3_shape[1] / 2), 2)

reshaped_data = np.concatenate([star2,star3],2)
reshaped_data = reshaped_data.reshape(star2_shape[0],star2_shape[1] * 2)

print(reshaped_data)
print("Re_reshaped_data = ", reshaped_data.shape)

np.savetxt("./TBP_sim/build/data_for_learning/Re_initial_value.csv", \
        initial)
np.savetxt("./TBP_sim/build/data_for_learning/Re_forward_step_data.csv", \
        reshaped_data)
