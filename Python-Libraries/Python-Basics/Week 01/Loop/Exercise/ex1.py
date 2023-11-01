n = int(input("Enter You Input: "))
for i in range(0,n,1):
    for j in range(1,n-i,1):
        print(j, end=" ")
    print()