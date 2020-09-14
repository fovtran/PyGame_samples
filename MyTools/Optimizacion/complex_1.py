# -*- coding: utf-8 -*-
import os
import math as m
import cmath as c
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
# import mathutils as mu

point = lambda x,y: tuple((x, y))
mid = lambda x,x1: (x-x1)/2  # x - x'
midpoint = lambda __a,__b: ( (__b[0] - __a[0])/2, (__b[1] - __a[1])/2 )
decomp = lambda _P,order: [_P[n][order] for n in range(len(_P))] # ejes i
decomp2d = lambda p, order: decomp(p,order)
conjugate2d = lambda P: [decomp2d(P,0), decomp2d(P,1)]  # ejes XY
conjugate3d = lambda P: [decomp2d(P,0), decomp2d(P,1), decomp2d(P,3)] #ejes XY
inverse = lambda P: [x for x in zip(decomp2d(A,0), decomp2d(A,1))] # lista de ejes a point
conj = conjugate2d

a = point(0,0)
b = point(10,10)
A = [None, None]
A[0] = a
A[1] = b

fig,ax = plt.subplots(1)
ax.grid(True)
ax.plot(*conjugate2d(A), '*-')

a = point(0,0)
b = point(10,10)
A = [None, None, None]
A[0] = a
A[1] = midpoint(a,b)
A[2] = b

fig2, ax = plt.subplots(1)
ax.grid(True)
ax.plot(*conjugate2d(A), '*-')

# radio = rho
# polar_angle = theta
# azimuth = phi

# For any complex number z, the magnitude of z, |z|, is defined as  √ z . ~z
# they have opposite arguments which cancel. this is always the usual principal square root defined on nonnegative real numbers.
# |Z| = |a + bi|  -> where a and b are complex and |v| is the magnitude of complex.
# |Z| = sqrt( a^2 + b^2 )
Z = sqrt(a**2 + b**2)
# phy -90 hasta 90
# phi 90 hasta 270
