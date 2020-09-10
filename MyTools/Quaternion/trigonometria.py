# -*- coding: utf-8 -*-
import time
import math
import numpy as np
from numpy import arcsin
import matplotlib.pyplot as plt
import __future__

# Functions
s = 0
v = 31

# beta distribution
# a-1 / a + b - 2
# absolute distribution
# 2*a exp a * b exp b  / B(a,b) * (a+b) exp a+b+1

y = lambda x: np.arcsin(np.sqrt(x))
y0 = lambda x: (np.arcsin(2*x -1) / np.pi ) + 1/2
t = (0., 30., 45., 60., 90., 180.)

s = np.array(t ) * np.pi / 360
sx = lambda x: [y0(n) for n in x]
sy = lambda x: [y(n) for n in x]

x = np.linspace(-2* np.pi , 2* np.pi * 2, 127)
_x = np.linspace(-2*np.pi, 2 * np.pi , 127)
y1 = y(x)
y2 = np.sin(2*x-1) + 3 * (np.arctan(2*x- np.pi) / np.pi)
y3 = sy(x)
y4 = sx(x)

fig1 = plt.figure()
#l, = plt.plot([], [], 'r-')
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y1, x, y2 , x, y4)
plt.xlim(-2, 8)
plt.ylim(-5, 5)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.grid()
plt.legend(loc=3)
plt.title('Inverse Trigonometry test')
#fig2 = plt.figure()
plt.show()