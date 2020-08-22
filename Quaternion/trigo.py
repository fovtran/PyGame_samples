# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

n = [-360,-180,-90,-2,-1,0,1,2,90,180,360]

for a in n:
    s = np.sin(a)
    c = np.cos(a)
    h = np.tan(a)
    print("cos(%.3f) = %.3f" % (a,c))
    print("sin(%.3f) = %.3f" % (a,s))
    print("tan(%.3f) = %.3f" % (a,h))