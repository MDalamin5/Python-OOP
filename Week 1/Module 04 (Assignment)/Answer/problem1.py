str = input()
count_l=0
count_r=0
current_str= ''
blance_str=[]
for char in str:
    if char =='L':
        count_l+=1
    elif char =='R':
        count_r+=1
    current_str+=char

    if count_l==count_r:
        blance_str.append(current_str)
        current_str=''
        count_l=0
        count_r=0

print(len(blance_str))
for data in blance_str:
    print(data)