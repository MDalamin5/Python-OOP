def solve():
    freq = {}
    N = int(input())
    numbers = list(map(int,input().split()))

    for number in numbers:
        freq[number] = 0
    
    for number in numbers:
        freq[number] += 1

    count = 0

    for key in freq:
        if freq[key] < key:
            count += freq[key]
        else:
            count += freq[key] - key
    
    print(count)

solve()