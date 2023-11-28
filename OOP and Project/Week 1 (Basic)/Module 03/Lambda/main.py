# def doubled(x):
#     return 2*x

# result = doubled(2)
# print(result)

result = lambda x: x*2
print(result(6))

fiver = lambda x,y,z: x*y*z
print(fiver(4,3,4))

# python MAP
numbers = [1,2,4,45,33,24,56,32,45,64,36]
# doubled_num = map(result, numbers)

doubled_num = map(lambda x:x*2, numbers)
print(numbers)
print(list(doubled_num))

actors = [
    {'name': 'Sabana', 'Age':65},
    {'name': 'Sahila Noor', 'Age':25},
    {'name': 'Sabnoor', 'Age':445},
    {'name': 'sumi', 'Age':70},
    {'name': 'Hard dick', 'Age':35}
]

juniors = filter(lambda actor : actor['Age']<30, actors)
fivers = filter(lambda actor: actor['Age']%2==0,actors)
print(list(fivers))
print(list(juniors))
