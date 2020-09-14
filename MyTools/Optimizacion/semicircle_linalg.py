# -*- encoding: utf-8 -*-
#from transformations import *
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

_2d=True
_3d=False
# theta from 45° to 66° in 12 steps
# c = 2*pi = 360
angle = 180
step = 12
rangle = angle * (2*np.pi / 360)
theta = np.linspace(-np.pi/2, -np.pi/2 -  rangle, step)
radio = 2
arc = radio * np.cos(theta)
y = radio * np.sin(theta)

z = np.linspace(0, 3, step)

if _2d:
    plot(arc, y)
    xlim([-5,5])
    ylim([-5,5])
    grid(True)
    show()

if _3d:
    x,y = np.meshgrid(arc,y)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim([-5,5])
    ax.set_ylim([-5,5])
    ax.set_zlim([-5,5])
    ax.grid(True)
    ax.plot_surface(x,y,z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
    plt.show()