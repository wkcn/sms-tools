import A4Part2
import numpy as np


def test(inputFile, window, M, N, H, SNR1, SNR2):
    SNR1_out, SNR2_out = A4Part2.computeSNR(inputFile, window, M, N, H)
    print((SNR1_out, SNR2_out), (SNR1, SNR2))
    np.testing.assert_allclose(SNR1_out, SNR1, atol=10, rtol=0)
    np.testing.assert_allclose(SNR2_out, SNR2, atol=100, rtol=0)


test('../../sounds/piano.wav', 'blackman', 513, 2048, 128, 67.57, 304.68)
test('../../sounds/sax-phrase-short.wav', 'hamming', 512, 1024, 64, 89.51,306.19)
test('../../sounds/rain.wav', 'hann', 1024, 2048, 128, 74.63,304.27)
