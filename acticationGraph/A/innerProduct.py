#
# 행렬의 내적
#

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

innnerMatrix = np.dot(x.T, y)

print (innnerMatrix)