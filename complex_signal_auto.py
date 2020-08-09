import numpy as np
from matplotlib.pyplot import *

file = './Peter Gabriel - Steam.wav'
#f = open('C:\Users\diego2\Documents\Sound 2.wav', 'ro')
signal2 = np.fromfile(open(file),np.float32)[24:]
print("signal read ok with a size of", len(signal2))
print(signal2[:16])

signal3 = np.abs(signal2)
print("signal process abs() of", len(signal3))
print(signal3[:16])

#signal4 = np.log10(signal2)
#print("final calculation is ", len(signal4))
#print(signal4[:16])

spectrum = np.fft.rfft(signal2[::8])
print("spectrum len is ", len(spectrum))
plot(spectrum)
#plot(10 * np.log10(abs(signal2)))
show()
