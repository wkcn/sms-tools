import A4Part4
from loadTestCases import load
import numpy as np


for i in range(1, 4):
    case = load(4, i)
    gt = case['output']
    output = A4Part4.computeODF(**case['input'])
    err = float(np.max(np.abs(output - gt)))
    print(f"Test case {i} error: {err}")
