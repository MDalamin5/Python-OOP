test_case = int(input())
count = 1
while count<=test_case:
    data = int(input())
    arr=[]
    while data!=0:
        rem = data%10
        arr.append(rem)
        data //=10
    output = ' '.join(str(element) for element in arr )  
    print(output)  
    count +=1 


