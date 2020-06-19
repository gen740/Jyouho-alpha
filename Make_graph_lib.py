import numpy as np
import matplotlib.pyplot as plt


def my_xyaxes(a_ax, xl=[-10, 10], yl=[-10, 10], color='k', size=20, latex=True):
    if latex:
        plt.rc('text', usetex=True)  # make annotation by latex

    arrow_dict = dict(arrowstyle="<-", color=color)

    a_ax.set_xlim(xl)
    a_ax.set_ylim(yl)
    x_width = xl[1] - xl[0]
    y_width = yl[1] - yl[0]  # determine xy limit

    a_ax.annotate('', xy=[xl[0], 0], xytext=(xl[1], 0), size=size, arrowprops=arrow_dict)
    a_ax.annotate('', xy=(0, yl[0]), xytext=(0, yl[1]), size=size, arrowprops=arrow_dict)
    a_ax.annotate(r'$x$', xy=(xl[1] - 1, 1), xytext=(xl[1] - 0.4 * x_width / 20, 0.2 * x_width / 20), size=size)
    a_ax.annotate(r'$y$', xy=(0, yl[1]), xytext=(0.2 * y_width / 20, yl[1] - 0.4 * y_width / 20), size=size)
    """
    draw xy axis and annotate 'x' and 'y'
    """