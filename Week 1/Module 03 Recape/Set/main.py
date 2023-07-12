# set is a unique collection items
numbers = [12,32,56, 98,12,6,98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(44)
print(numbers_set)
numbers_set.remove(98)
print(numbers_set)
for item in numbers_set:
    print(item)

if 44 in numbers_set:
    print('Yes')

A = {1,3,4,5,6,7}
B = {2,1,4,5,3}
print(A&B)
print(A | B)