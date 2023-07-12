numbers = [12, 56, 98, 33, 23, 23, 33, 54]
# Kye value pair
# dictionary
# object
# hash table

person = {"Name":"Al Amin", "Profecion":"Student", "Age":23,"Address":"Bashundhara"}
print(person)
print(person["Age"])
print(person.keys())
print(person.values)
person["Language"]="Python"
print(person)
person["Name"]="Md Al Amin"
print(person)
del person["Age"]
print(person)

# looping
for item in person:
    print(item)
# spatial looping
for key, value in person.items():
    print(key, value)
