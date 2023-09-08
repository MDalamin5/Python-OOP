class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []
    
    def add_to_cart(self, item):
        self.cart.append(item)

Alamin = Shop('Al Amin')
Alamin.add_to_cart('Book')
Alamin.add_to_cart('pencel')
Alamin.add_to_cart('Pencele')
print(Alamin.cart)

Kaysar = Shop('Kaysar')
Kaysar.add_to_cart('Tshirt')
Kaysar.add_to_cart('Shirt')
Kaysar.add_to_cart('pant')
Kaysar.add_to_cart('Watch')
print(Kaysar.cart)