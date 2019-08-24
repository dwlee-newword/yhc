import numpy as np

# 행렬
listA = [
    [1, 2], 
    [3, 4]
    ]
listB = [
    [5, 6], 
    [7, 8]
    ]

matrix_A = np.array(listA)
matrix_B = np.array(listB)

# 두 행렬의 합
print(matrix_A + matrix_B)

# 두 행렬의 곱
print(matrix_A @ matrix_B)