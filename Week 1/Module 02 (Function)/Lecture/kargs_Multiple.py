def full_name(first, last):
    name = f"Full name is: {first} {last}"
    return name

# take parameter in order
# name = full_name("Md", "Al Amin")
name = full_name(last="Al Amin", first="Md")
# print(name)

def famous_Name(fist,last, **additional):
    name = f"{fist} {last}"
    #print(additional["title"])
    for key, value in additional.items():
        print(key, value)
    return name

name = famous_Name(fist="Md", last="Al Amin", title = "Hello", podobe="Mondol", additional="Mondol")
print(name)

def a_lot(num,num2):
    sum=num+num2
    mul= num*num2
    rem=num%num2
    return sum,mul,rem

everething = a_lot(10,3)
print(everething)