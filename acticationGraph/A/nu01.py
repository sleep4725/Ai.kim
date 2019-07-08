import numpy as np

mat = np.array(
    [[1, 2, 3],
     [4, 5, 6]])

#
# matrix의 차원
# ndim : 차수
print (np.ndim(mat))

#
# shape
# (2, 3)
print (np.shape(mat))

#
# dtype
# 데이터 타입/ int32
print (mat.dtype)