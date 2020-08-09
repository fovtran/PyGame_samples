import numpy as np
from matplotlib.pyplot import *

x = np.arange(256.0)
sin1 = np.sin(2 * np.pi * (1250.0 / 10000.0) * x)
sin2 = np.sin(2 * np.pi * (625.0 / 10000.0) * x)

signal = sin1 + sin2
print(signal)
plot(signal)

spectrum = np.fft.rfft(signal)
#plot(spectrum)
#show()
#plot(abs(spectrum))
#show()
#plot(10 * np.log10(abs(spectrum)))
#show()
#spectgram = np.specgram(signal)
