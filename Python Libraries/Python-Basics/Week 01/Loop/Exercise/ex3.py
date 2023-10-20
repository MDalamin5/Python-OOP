dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
result = []

for i in range(1,8):
    result.append(0)


for i in dice_result:
    result[i] +=1

print(result[6])
print(result[1])

    