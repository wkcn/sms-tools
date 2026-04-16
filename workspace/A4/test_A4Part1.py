import A4Part1


def test(window, M, num_samples):
    mX = A4Part1.extractMainLobe(window, M)
    assert len(mX) == num_samples


test('blackmanharris', 100, 65)
test('boxcar', 120, 17)
test('hamming', 256, 33)
