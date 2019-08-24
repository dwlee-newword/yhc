# 1D list
listA = [1, 3, 5, 7]
listB = [2, 4, 6, 8]

# 두 vector의 합은?

result_list = []
for a, b in zip(listA, listB):
    result_list.append(a+b)

print(result_list)

# vector의 단순 곱은?

result_list = []

for a in listA:
    result_list.append(a*10)

print(result_list)

# 두 vector의 곱은?

result_list = []

for a, b in zip(listA, listB):
    result_list.append(a * b)

print(result_list)

# 두 vector의 내적(dot product)
sum_of_multi = 0
for res in result_list:
    sum_of_multi = sum_of_multi + res
    
print(sum_of_multi)


# 두 vector의 거리
import math
sum_of_distance = 0
for a, b in zip(listA, listB):
    sum_of_distance = sum_of_distance + math.pow(a - b, 2)

distance_result = math.sqrt(sum_of_distance)

print(distance_result)