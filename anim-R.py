import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from ast import literal_eval

data = np.loadtxt("./TBP_sim/build/data_for_learning/Re_forward_step_data.csv")

print(data.shape)
data_shape=data.shape

star2_mask, star3_mask   = [], []
star1, star2, star3      = [], [], []

for i in range(int(data_shape[1]/4)):
    star2_mask = np.append(star2_mask,np.array([True,True,False,False]))
    star3_mask = np.append(star3_mask,np.array([False,False,True,True]))

star2 = data[:,np.array(star2_mask,dtype=bool)]
star3 = data[:,np.array(star3_mask,dtype=bool)]

print(star2.shape)

COG = (star2 + star3) / 3

star1 = - COG
star2 = star2 - COG
star3 = star3 - COG

for i in range(100):
    star1_data = star1[i]
    star2_data = star2[i]
    star3_data = star3[i]

    data_shape_2 = COG.shape

    star1_data = star1_data.reshape(int(data_shape_2[1]/2),2)
    star2_data = star2_data.reshape(int(data_shape_2[1]/2),2)
    star3_data = star3_data.reshape(int(data_shape_2[1]/2),2)

    fig, ax = plt.subplots(dpi = 400, figsize=(10,8))

    ax.plot(star1_data[:,0],star1_data[:,1],".", markersize = 0.3)
    ax.plot(star2_data[:,0],star2_data[:,1],"r.", markersize = 0.3)
    ax.plot(star3_data[:,0],star3_data[:,1],"b.", markersize = 0.3)

    fig.savefig(f"./Result/figure{i + 1}.png")
    plt.clf()
    fig.clf()
