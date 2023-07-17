N, M = input().split() 
N = int(N)
M = int(M)

A = input().split() 
A = [int(num) for num in A]


occurrences = [0] * M
for num in A:
    occurrences[num-1] += 1


for i in range(1, M+1):
    count = 0
    for num in A:
        if num == i:
            count += 1
    print(count)
