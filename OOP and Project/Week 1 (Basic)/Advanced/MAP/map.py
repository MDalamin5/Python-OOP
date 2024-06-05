def getEven(num):
    if num % 2 == 0:
        return num
    

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNum = list(map(getEven, data))
print(evenNum)