# n = input("Enter Your Input: ")
# print(n)
# n = int(n)
# if n%2==0 and not n>23:
#     print('even')
# else:
#     print('ODD')
bangal = ['Shingra', 'Baguni', 'Puri', 'jalabi']
indian = ['Dal Vaji', 'Naan', 'Ruti']
italian = ['Egg role', 'pot sticker', 'Fride rice']

dish = input('Enter your Dish Name: ')

if dish in bangal:
    print(f'{dish} is a Bangle Food')
elif dish in indian:
    print(f'{dish} is Indian Food')
elif dish in italian:
    print(f'{dish} is Italian Food')
else:
    print(f'I don"t know {dish} food')

