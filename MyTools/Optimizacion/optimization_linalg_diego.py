import numpy as np

# Array algo
x = np.array(np.random.rand(30), dtype=np.float64)
x1 = np.array(np.random.rand(12), dtype=np.float64)

size = x.size + x1.size

stream = np.zeros(size, dtype=np.float64)
concat = np.concatenate((x,x1))
stream[:] = np.sort(concat)

# Matrix algo
N_size = 30
M_size = 15

N = np.matrix((np.random.rand(N_size), np.random.rand(N_size), np.random.rand(N_size)), dtype=np.float64)
M = np.matrix((np.random.rand(M_size), np.random.rand(M_size), np.random.rand(M_size)), dtype=np.float64)

# Sample object
N = [[ 0.65060472,  0.28127748,  0.46373757],
       [ 0.15119803,  0.29792385,  0.45769395],
       [ 0.92816929,  0.70244273,  0.19984391]]
       
M = [[ 0.6327318 ,  0.981731  ,  0.08330851],
       [ 0.0200211 ,  0.77826689,  0.92665106]]
       
# Hipotesis:

# para cada N
i,j,k = N[:,0]
i = 0.30543891
j = 0.75541763
k = 0.17363018

i = 0.72438268
j = 0.7960738
k = 0.69920185

# Concatenar valores ijk para N,M en pos = 0.
pos = 0
def reconcat(_N, _M, pos):
	#concat N_ijk con M_ijk y reshape(2,3) para size=2, 3 ejes
	NM = np.concatenate((_N[:,pos],_M[:,pos])).reshape(2,3) 
	i = np.concatenate((_N[:,pos],_M[:,pos])).reshape(1,3)[:,0]
	j = np.concatenate((_N[:,pos],_M[:,pos])).reshape(1,3)[:,1]
	k = np.concatenate((_N[:,pos],_M[:,pos])).reshape(1,3)[:,2] 
	return np.matrix((i,j,k), dtype=np.float64)

N = np.random.rand(200,3)
M = np.random.rand(100,3)	

for pos in range(0,N.size):
	mat = reconcat(N,M,pos)
	print(mat)