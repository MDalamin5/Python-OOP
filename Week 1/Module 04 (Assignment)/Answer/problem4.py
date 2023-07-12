n = int(input())
numbers = []
for i in range(0,n):
    data = int(input())
    numbers.append(data)
count = 0
result =0
for i in numbers:
    if(i%2==0):
        numbers.append(i/2)
        count+=1
        if(count==n):
            result+=1
            count=0
    else:
        break
print(result)