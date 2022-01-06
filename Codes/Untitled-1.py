import numpy as np
from numpy.matrixlib.defmatrix import _convert_from_string

c = np.array(input().split(' '))
c = _convert_from_string(c)
print(c[2])