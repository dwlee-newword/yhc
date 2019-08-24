import numpy as np

listA = [
    [1, 2], 
    [3, 4]
    ]
listB = [
    [5, 6], 
    [7, 8]
    ]

vectorA = np.array(listA)
vectorB = np.array(listB)

print(vectorA * vectorB)
