numbers = [1,3,45,5,64,4]
numbers.append(7)
print(numbers)
numbers.insert(0,44)
print(numbers)
numbers.remove(45)
print(numbers)
if 3 in numbers:
    numbers.remove(3)
    
print(numbers)
if 33 in numbers:
    numbers.remove(33)
else:
    print("33 is not your list")

print(numbers)
print(numbers.pop())
print(numbers)
print("Index of 64: ",numbers.index(64))
sorted = numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)