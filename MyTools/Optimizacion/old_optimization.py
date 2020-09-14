import numpy as np

x = np.zeros((3, 5, 2), dtype=np.complex128)
x.size
x.shape

nul = np.array([1,3,5], dtype=np.float64)

a = np.array(np.random.rand(30), dtype=np.float64)
b = np.array(np.random.rand(12), dtype=np.float64)

size = a.size + b.size

c = np.zeros(size, dtype=np.float64)

fin = list(a)+list(b)
np.sort(fin)
np.array(fin)