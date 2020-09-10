#!env python.exe
# -*- coding: utf-8 -*-
"""\
A simple demo of logging configuration with YAML (Python 2.7)
=============================================================

Requires PyYAML -> "easy_install PyYAML"

See the recipes for configuring logging with dicts and YAML
- http://docs.python.org/2.7/howto/logging-cookbook.html
"""

import unittest
import numpy as np
np.set_printoptions(precision=15)

__title__ = 'example'
__author__ = "DMC Creations."
__credits__ = ["Diego Cadogan."]
__email__ = "dcadogan@live.com.ar"
__version__ = "0.2.0"
__status__ = "Alpha"
__maintainer__ = "DMC"
__license__ = "GPL"
__copyright__ = "Copyright 2016, "

import os
from math import *
import cmath
from matplotlib.pyplot import *
import sympy as sy
import numpy as np

np.radians(-360)==-6.2831853071795862
np.radians(-270)==-4.7123889803846897
np.radians(-180)==-3.1415926535897931
np.radians(-90)==-1.5707963267948966
np.radians(0)==0.0
np.radians(90)==1.5707963267948966
np.radians(180)==3.1415926535897931
np.radians(270)==4.7123889803846897

def Cos(a): return cos(radians(a))
def Sin(a): return sin(radians(a))
def Tan(a): return tan(radians(a))
def ArcTan(a):  return degrees(arctan(a))
def ArcSin(a):  return degrees(arcsin(a))
def ArcCos(a):  return degrees(arccos(a))
def ToRad(a): return a*pi/180  # convert to rad

X = complex(0, 0j)
Y = complex(0, 1j)
Z = complex(0, 2j)
W = complex(-1, 3j)
S = [X,Y,Z, W]
Q = [0,1,2,3]

#plot(S, '*-')
def T(a,n):
    while a<=n:
        yield a
        a+=1

x = sy.Symbol('x')
t = sy.Symbol('t')
x = sy.tanh(t**3)
sy.plot(x, (t, -1.5, 0), line_color = 'red')
