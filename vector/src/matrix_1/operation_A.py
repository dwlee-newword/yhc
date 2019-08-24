# 행렬
listA = [
    [1, 2], 
    [3, 4]
    ]
listB = [
    [5, 6], 
    [7, 8]
    ]


# 두 행렬의 합
outterList = []
for A, B, in zip(listA, listB):

    innerList = []
    for a, b in zip(A, B):
        innerList.append(a + b)
    outterList.append(innerList)

print(outterList)

# 두 행렬의 곱
