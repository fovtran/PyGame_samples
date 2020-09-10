import numpy as np
from numpy import arange, exp
import matplotlib.pyplot as plt


t=arange(0,10,0.01)
q=1-exp(-0.5*t)
i=0.5*exp(-0.5*t)
v=10*(1-exp(-0.5*t))

fig,ax = plt.subplots()
ax.plot(t, q, 'k--', label='charge')
ax.plot(t, i, 'k:', label='current')
ax.plot(t, v, 'k', label='voltage')
plt.xlabel('Time')
plt.ylabel('Current')
plt.title('R-C Circuit')
plt.show()
