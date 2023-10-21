import numpy as np
from numba import njit

@njit(fastmath=True)
def fast_inverse_sqrt(number):
    threehalfs = 1.5
    x2 = number * 0.5
    y = np.float32(number)

    i = y.view(np.int32)
    i = np.int32(0x5f3759df) - np.int32(i >> 1)
    y = np.float32(i).view(np.float32)

    y = y * (threehalfs - (x2 * y * y))
    return float(y)

number = 25.0
inverse_sqrt = fast_inverse_sqrt(number)
print(inverse_sqrt)
## QUAKE SRC CODE [C ] 20XX - PYTHON
#---
# Path: hellov1.py
