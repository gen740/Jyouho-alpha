import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from ast import literal_eval


animation = True


with open("./TBP_sim/build/data/options.txt", 'r') as f:
    options = f.read()
options = literal_eval(options)
stars = []
for i in range(options['NUMBER_OF_STAR']):
    stars.append(np.loadtxt(f"./TBP_sim/build/data/star{i + 1}.csv"
        ,delimiter=' '))
fig, ax = plt.subplots()

if animation == False:
    for i in range(options['NUMBER_OF_STAR']):
        ax.plot(stars[i][:,0], stars[i][:,1], "b-")
    fig.savefig("./Result/Trajectory.png")

else:
    artists = []
    for i in range(len(stars[i][:,0])):
        xdata = []
        ydata = [] 
        for j in range(options['NUMBER_OF_STAR']):
            xdata.append(stars[j][i][0])
            ydata.append(stars[j][i][1])
        im = ax.plot(xdata,ydata,"b.")
        artists.append(im)
    ani = anm.ArtistAnimation(fig, artists, interval=10)
    ani.save('./Result/Trajectory_ani.mp4', writer="ffmpeg")
