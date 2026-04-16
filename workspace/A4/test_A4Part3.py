import A4Part3
import matplotlib.pyplot as plt


def test(inputFile, window, M, N, H):
    E = A4Part3.computeEngEnv(inputFile, window, M, N, H)
    plt.pcolormesh(E)
    plt.show()


test('../../sounds/piano.wav', 'blackman', 513, 1024, 128)
test('../../sounds/piano.wav', 'blackman', 2047, 4096, 128)
test('../../sounds/sax-phrase-short.wav', 'hamming', 513, 2048, 256)
