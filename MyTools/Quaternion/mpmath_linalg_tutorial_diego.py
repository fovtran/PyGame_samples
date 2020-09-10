from mpmath import *
mp.dps = 15; mp.pretty = True

# A basic 1D integral:
quad(sin, [0, pi])
# 2.0

# A basic 2D integral:

f = lambda x, y: cos(x+y/2)
quad(f, [-pi/2, pi/2], [0, pi])
# 4.0
