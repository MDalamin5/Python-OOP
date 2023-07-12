numbers = [45, 87, 65, 85,24, 36, 61]
ods = []
for num in numbers :
    if num%2 == 1 and num%5==0:
        ods.append(num)
print(ods)

odd_numbers = [num for num in numbers if num%2==1 if num%5==0]
print(odd_numbers)

players = ["Sakib", "Musfiq", "Liton"]
ages = [38,40, 25]
age_com = []

for player in players :
    print("Player: ", player)
    for age in ages:
        print(player, age)
        age_com.append([player, age])
print(age_com)

# list comperhensions
age_com2 = [[player, age] for player in players for age in ages]
print(age_com2)