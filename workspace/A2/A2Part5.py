import numpy as np

"""
A2-Part-5: Compute the magnitude spectrum (Optional)

Write a function that computes the magnitude spectrum of an input sequence x of length N. The 
function should return an N point magnitude spectrum with frequency index ranging from 0 to N-1.

The input argument to the function is a numpy array x and the function should return a numpy array of the 
magnitude spectrum of x.

EXAMPLE: If you run your function using x = np.array([1, 2, 3, 4]), the function should return the following 
numpy array magX: [array([10.0, 2.82842712, 2.0, 2.82842712])
"""
def genMagSpec(x):
    """
    Input:
        x (numpy array) = input sequence of length N
    Output:
        The function should return a numpy array
        magX (numpy array) = The magnitude spectrum of the input sequence x
                             (length N)
    """
    ## Your code here
    N = len(x)
    n = np.arange(0, N).reshape((N, 1))
    k = n.reshape((1, N))
    Sj = np.cos(2 * np.pi * k * n / N) - 1j * np.sin(2 * np.pi * k * n / N)
    X = x @ Sj
    return np.abs(X)
