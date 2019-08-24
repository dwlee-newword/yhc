import numpy as np
# 수학적 연산을 하는 라이브러리

# 2D array
vectorA = np.array([1, 3, 5, 7])
vectorB = np.array([2, 4, 6, 8])

# 두 vector의 합은?

print(vectorA + vectorB)

# list와 vector는 합에서 차이가 나는 것을 볼 수 있음

# vector의 단순(scala) 곱은?

print(vectorA * 2)

# 두 vector의 곱은?

print(vectorA * vectorB)

# 두 vector의 내적(dot product)

print(sum(vectorA * vectorB))

# 두 vector의 거리

print(sum((vectorA - vectorB)**2)**(1/2))