class Product:
    def __init__(self, name) -> None:
        self.name = name
        pass

class Shop(Product):
    def __init__(self, name) -> None:
        self.all_Product = []
        self.cart = []
        super().__init__(name)

    def add_product(self, item, price, quantity):
        product = {'item': item, 'price':price, 'quantity':quantity}
        self.all_Product.append(product)

    def buy_product(self, item):
        for i in range(len(self.all_Product)):
            if self.all_Product[i]['item']== item:
                self.cart.append(self.all_Product[i])
                print('Congress')

    def show_MyCart(self):
        for i in self.cart:
            print(i)


mahede_mart = Shop('Al Amin')
mahede_mart.add_product('Alu', 23, 3)
mahede_mart.add_product('Jal', 234, 5)
mahede_mart.buy_product('Alu')
mahede_mart.show_MyCart()
