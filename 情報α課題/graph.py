import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def make_graph(file_name):
    data = np.loadtxt("./DATA/data40.txt")
    print(data)

    fig1, ax1 = plt.subplots(dpi = 100, figsize = (12, 9))
    ax1.plot(data[:,1],data[:,2])
    ax1.set_xlabel("param_size")
    ax1.set_ylabel("Generalization loss")
    fig1.savefig(f"./graphs/{file_name}_loss.png")

    fig1, ax1 = plt.subplots(dpi = 100, figsize = (12, 9))
    ax1.plot(data[:,1],data[:,3])
    ax1.set_xlabel("param_size")
    ax1.set_ylabel("Generalization acc")
    fig1.savefig(f"./graphs/{file_name}_acc.png")
    
    fig1, ax1 = plt.subplots(dpi = 100, figsize = (12, 9))
    ax1.plot(data[:,1],data[:,5])
    ax1.set_xlabel("param_size")
    ax1.set_ylabel("A")
    fig1.savefig(f"./graphs/{file_name}_A.png")
    
    
    fig1, ax1 = plt.subplots(dpi = 100, figsize = (12, 9))
    ax1.plot(data[:,1],data[:,6])
    ax1.set_xlabel("param_size")
    ax1.set_ylabel("B")
    fig1.savefig(f"./graphs/{file_name}_B.png")
    

    fig1, ax1 = plt.subplots(dpi = 100, figsize = (12, 9))
    ax1.plot(data[:,1],data[:,7])
    ax1.set_xlabel("param_size")
    ax1.set_ylabel("C")
    fig1.savefig(f"./graphs/{file_name}_C.png")
