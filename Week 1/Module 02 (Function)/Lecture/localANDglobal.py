# global variable

total_blance = 10000
def buySomethings(item,pirce):
   # print(total_blance)
    global total_blance
    total_blance=total_blance-pirce
    output = f"You buying item is: {item} {pirce}"
    print("Balence left: ",total_blance)
    print(output)
buySomethings("Panjabe",300)