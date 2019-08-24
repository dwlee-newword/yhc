# 2D list
listA = [1, 3, 5, 7]
listB = [2, 4, 6, 8]

# 두 vector의 합은?

result_list = []
for a, b in zip(listA, listB):
    result_list.append(a+b)

print(result_list)

# vector의 단순(scala) 곱은?

result_list = []

for a in listA:
    result_list.append(a*10)

print(result_list)

# 두 vector의 곱은?

result_list = []

for a, b in zip(listA, listB):
    result_list.append(a * b)

print(result_list)

