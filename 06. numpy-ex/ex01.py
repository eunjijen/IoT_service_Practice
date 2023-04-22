import numpy as np

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)

print(type(a1))
#<class 'numpy.ndarray'>

print(a1, a1.dtype, a1.shape)
# [0 1 2 3 4 5] int32 (6,) --> tuple 1차원 data (6개의 elements)



data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)

print(a2, a2.dtype, a2.shape)
# [ 0.1  5.   4.  12.   0.5] float64 (5,)



np.array([0.5, 2, 0.01, 8])

a3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
a3.shape  # (4, 3)


np.arange(0, 10, 2)
# array([0, 2, 4, 6, 8])

np.arange(0, 10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


a1 = np.array([0, 10, 20, 30, 40, 50])
# array([ 0, 10, 20, 30, 40, 50])
a1

a1[5] = 70
# array([ 0, 10, 20, 30, 40, 70])

a1[[1, 3, 4]]  # 인덱스 1, 3, 4번을 뽑아달라
# array([10, 30, 40])





