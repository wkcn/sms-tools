import numpy as np
import matplotlib.pyplot as plt
from A3Part2 import optimalZeropad


def test(f, M, fs):
    t = np.arange(M) / fs
    x = np.cos(2 * np.pi * f * t)
    mX = optimalZeropad(x, fs, f)

    M = len(x)
    N = (len(mX) - 1) * 2
    pad = N - M

    fig, (ax1, ax2) = plt.subplots(2, 1)

    plt.suptitle(f"f={f}, M={M}, fs={fs}, pad={pad}")

    ax1.set_title("Input Signal")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Amplitude")
    ax1.plot(t, x)

    num_non_zero = sum(mX > -240)
    i = np.argmax(mX)
    k = np.arange(len(mX)) * (fs / N)
    ax2.set_title(f"DFT Spectrum, #non-zero={num_non_zero}, length={len(mX)}, max_index={i}, freq={k[i]}")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Magnitude (dB)")
    ax2.plot(k, mX)

    plt.show()


test(f=100, M=25, fs=1000)
test(f=250, M=210, fs=10000)
