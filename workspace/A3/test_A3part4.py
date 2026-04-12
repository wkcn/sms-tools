import numpy as np
import matplotlib.pyplot as plt
from A3Part4 import suppressFreqDFTmodel
from scipy.fftpack import fft


def gen_signal(freqs, fs, M):
    t = np.arange(M) / fs
    x = np.zeros(M)
    for f in freqs:
        x += np.cos(2 * np.pi * f * t)
    return x


def get_magnitude(x):
    M = len(x)
    X = fft(x)
    mX = 20 * np.log10(abs(X))[:M//2 + 1]
    return mX


def test(freqs):
    fs = max(freqs) * 2
    seconds = 1
    M = int(seconds * fs)
    x = gen_signal(freqs, fs, M)
    N = 2 ** int(np.ceil(np.log2(M)))
    y, yfilt = suppressFreqDFTmodel(x, fs, N)

    mX = get_magnitude(x)
    mY = get_magnitude(y)
    mYfilt = get_magnitude(yfilt)

    k = np.arange(len(mX)) * (fs / M)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    ax1.set_title(f"mX {freqs}")
    ax1.plot(k, mX)

    ax2.set_title(f"mY {freqs}")
    ax2.plot(k, mY)

    threshold = 70
    freqs_filt = [f for f in freqs if f > threshold]
    ax3.set_title(f"mYfilt {freqs_filt}")
    ax3.plot(k, mYfilt)
    plt.show()


test([40, 100, 200, 1000])
test([23, 36, 230, 900, 2300])
