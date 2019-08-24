# 2D list
listA = [1, 3, 5, 7]
listB = [2, 4, 6, 8]

# list와 vector의 연산 차이 
# 두 리스트의 합은?


result_list = []
for a, b in zip(listA, listB):
    result_list.append(a+b)

print(result_list)

# 리스트의 단순(scala) 곱은?

result_list = []

for a in listA:
    result_list.append(a*10)

print(result_list)

# 두 리스트의 곱은?

result_list = []

for a, b in zip(listA, listB):
    result_list.append(a * b)

print(result_list)

