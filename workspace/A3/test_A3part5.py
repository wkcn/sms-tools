import numpy as np
import matplotlib.pyplot as plt
from A3Part5 import zpFFTsizeExpt

M = 512
f = 110
fs = 1000

t = np.arange(M) / fs
x = np.cos(2 * np.pi * f * t)

fft_sizes = [256, 512, 512]
mXs = zpFFTsizeExpt(x, fs)

max_freq = max(map(len, mXs)) * (fs / min(fft_sizes))

fig, axs = plt.subplots(3, 1, figsize=(10, 10))
for ax, fft_size, mX in zip(axs, fft_sizes, mXs, strict=True):
    k = np.arange(len(mX)) * (fs / fft_size)
    ti = np.argmax(mX)
    ax.set_title(f"{k[ti]}")
    ax.plot(k, mX)
    ax.set_xlim(0, max_freq)
plt.show()
