
# list ----> []
# tuple ----> ()
# set ------> {}
# set: is unique collection no dupicate
numbers = [12,56,98,33,23,23, 33,54]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(32)
print(numbers_set)
numbers_set.remove(54)
print(numbers_set)
for item in numbers_set:
    print(item)
if 23 in numbers_set:
    print("Yes")

A = {1,3,5}
B = {1, 2,4,5,3}
print("Intersection: ",A & B) # intersection
print ("Union: ",A | B)