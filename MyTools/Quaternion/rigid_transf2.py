import cmath as mth
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

t1 = np.linspace(0, 2 * np.pi, 11)
t2 = np.linspace(0, 2 * np.pi, 50)
print ("Len A: ", len(t1), "  -- Len B: ", len(t2))
x1 = np.cos(t1)
y1 = np.sin(t1)
x2 = np.cos(t2)
y2 = np.sin(t2)

plt1 = plt.plot(x1,y1,'bo', label='tuple')
plt2 = plt.plot(x2,y2,':k', label='vertex')
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

a = sc.linspace(-2j, 2j, 20)
b = sc.linspace(-np.pi, np.pi, 20)
c = sc.linspace(np.pi, -np.pi, 20)
m = [b] + [c]

A = np.cos(a)
B = np.sin(b)
C = np.cos(c)
M = [C]+[B]
i, mm = [ x for i,x in enumerate(M)]