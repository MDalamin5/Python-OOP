class Shopping:
    def __init__(self, name):
        self.name= name
        self.cart = []
    
    def add_to_cart(self, item, price,quantity):
        product = {'item': item, 'price':price, 'quantity':quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total =0
        for product in self.cart:
            total += product['price']*product['quantity']
        
        print(f'Total amount {total}')
        if amount<total:
            print(f'You have less amount. Please give more {total-amount} Taka')
        else:
            print(f'Checkout Sussfully')
            print(f'Your left amount {amount-total} taka')
            print('Thank you for shopping here!!')

    def removeItem(self, item):
        for i in range(len(self.cart)):
            if self.cart[i]['price']== item:
                del self.cart[i]
                print(f'{item} remove sussfully')
                break

Alamin = Shopping('Al Amin')
Alamin.add_to_cart('Alu', 30, 1)
Alamin.add_to_cart('Piaz', 80, 1)
Alamin.add_to_cart('Salt',40,1)
for product in Alamin.cart:
    print(product)

Alamin.removeItem(80)
Alamin.checkout(500)
for product in Alamin.cart:
    print(product)
