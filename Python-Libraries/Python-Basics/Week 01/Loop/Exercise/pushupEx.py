total_pushUp = 0
coutn = 0

while total_pushUp < 50:
    total_pushUp += 1
    coutn += 1
    print('Push Up')

    if(coutn == 10):
        answer = input("Are You Tired wnat to break: ")
        if(answer == 'n'):
            coutn = 0
            continue
        else:
            break
    
else:
    print("congrasulation You did 50 Push up")

print('Total push up', total_pushUp)