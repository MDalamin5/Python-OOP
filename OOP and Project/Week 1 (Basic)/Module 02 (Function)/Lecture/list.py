# list , array , collection is same

# index =  0.   1   2.  3.  4.  5  6.  7    8.  9
numbers = [11, 23, 44, 42, 45, 55, 33, 54, 66, 87]
# index = -10. -9  -8 -7. -6 -5    -4. -3  -2. -1
print(numbers)
print(numbers[4], numbers[-2])

# list (start : end)
print(numbers[2:6])
print(numbers[1:8])

# list (start : end : step)
print(numbers[1:7:1])
print(numbers[1 : 9 : 2])
print(numbers[2:7:-1])
print(numbers[7:2:-1])
print(numbers[7:2:-3])
print(numbers[4:])
print(numbers[:5])
print(numbers[:])      # shortcut to copy a list
print(numbers[::-1])   # shortcut to reverse a list