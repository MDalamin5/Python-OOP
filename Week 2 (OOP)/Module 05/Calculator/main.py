class calculator:
    brand = 'Apple'

    add = lambda self, x,y : x+y
    multiaplicattion = lambda self, x,y :x*y
    didiction = lambda self, x,y : x-y
    divition = lambda self, x,y : x//y

ob = calculator()
print("Sum of 2 and 3 = ",ob.add(2,3))
print('Multiaplicaton of 2 and 4 = ',ob.multiaplicattion(2,4))
print('Didtion of 3 and 2 = ',ob.didiction(3,2))
print('Diviton  of 4 and 2 = ', ob.divition(4,2))