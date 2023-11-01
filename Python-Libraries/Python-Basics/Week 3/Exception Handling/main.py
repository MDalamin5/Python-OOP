a = int(input('Enter a integer :'))
b = int(input("Enter another integer: "))

try:
    print(a/b)

except Exception as e:
    print(e)
    print('Exception is Cought.')

print("Ist last line of the code.")