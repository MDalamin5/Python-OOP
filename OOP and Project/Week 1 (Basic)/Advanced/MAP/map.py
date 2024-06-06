def makeEven(num):
    if num % 2 == 0:
        return num
    else:
        return num + 1
    

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNum = list(map(makeEven, data))
print(evenNum)