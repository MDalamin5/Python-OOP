name = 'Sakib\'s Khan'
name2 = "sakib khan"
# multiline 
name3 = """
Sakib Kahn
Number one
        """
print(name3)
print(name)
# mutable means changeable
# immutable means you can not change it
# string is a sequence of charecter

for char in name2:
    print(char)
print(name2[3])
print(name2[1:6])
print(name[-3])
print(name2[::-1])
# name2[0] = 'R'
print(name2)
if 'khan' in name2:
    print("Exists")
else:
    print('no')

print(name2.upper())

