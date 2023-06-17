def spatial_Fun(num1,num2,*numbers):
    print(numbers)
    sum=0
    for i in numbers:
        sum+=i;  
    return sum
all_sum = spatial_Fun(4,2,2)
print(all_sum)