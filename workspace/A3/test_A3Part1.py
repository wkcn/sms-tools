import numpy as np
import matplotlib.pyplot as plt
from A3Part1 import minimizeEnergySpreadDFT


def test(fs, f1, f2):
    seconds = 10
    n = int(fs * seconds)
    t = np.arange(n) / fs
    x1 = np.cos(2 * np.pi * f1 * t)
    x2 = np.cos(2 * np.pi * f2 * t)
    x = x1 + x2
    mX = minimizeEnergySpreadDFT(x, fs, f1, f2)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    plt.suptitle(f"fs={fs}, f1={f1}, f2={f2}")

    ax1.set_title("Input Signal")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Amplitude")
    ax1.plot(t, x)

    num_non_zero = sum(mX > -240)
    ax2.set_title(f"DFT Spectrum, #non-zero={num_non_zero}")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Magnitude (dB)")
    M = (len(mX) - 1) * 2
    k = np.arange(len(mX)) * (fs / M)
    ax2.plot(k, mX)

    plt.show()

test(fs=10000., f1=80., f2=200.)
test(fs=48000., f1=300., f2=800.)
