# list in 3rd bracket but Tuple data stay in first braket
def multipule():
    return 3,4
# print(multipule())

things = "pen", "Pencel", "Botol", "Labtop", "Web Cam", "Hair ban", "Glass"
print(things)
print(things[::-1])
if "Botol" in things:
    print("Yes I'm Here")
else:
    print("No i'm not here")
# print(things[2:6])
for items in things:
    print(items)
# things[0] = "Bag"
print(len(things))