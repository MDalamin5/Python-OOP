num1= input("Enter a integer number: ")
num2= input("Enter a integer number: ")
num3= input("Enter a integer number: ")

num1_int = int(num1)
num2_int = int(num2)
num3_int = int(num3)

if num1_int>num2_int and num1_int>num3_int:
    print("Number one is large: ",num1_int)
elif num2_int>num1_int and num2_int>num3_int:
    print("Number two is large: ",num2_int)
else:
    print("Num3 is large: ",num3_int) 

    