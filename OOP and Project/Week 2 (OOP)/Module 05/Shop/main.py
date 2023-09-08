class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

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
print(Kaysar.cart)