class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity
        

class Store:
    def __init__(self) -> None:
        self.__product_price = {}
        self.__product_quantity = {}
        self.__profit = 0

    def add_product(self, name, price, quantity): 

        product = Product(name,price, quantity)

        self.__product_price[product.product_name] = product.product_price
        self.__product_quantity[product.product_name] = product.product_quantity

    def display_product(self):
        
        print('All products price: ', self.__product_price)
        print('All product Quantity: ', self.__product_quantity)


    def buy_product(self, name, quantity):
        if name in self.__product_price:
            if self.__product_quantity[name] >=quantity:
                
                #profit calculation
                self.__profit += ((5* self.__product_price[name])/100)*quantity

                self.__product_quantity[name] -= quantity
                print(f'{name} add your cart sussfully')
            
            else:
                print(f'This {name} is unalible')
        else:
            print('Product no found')

    def get_profit(self):
        return self.__profit


class Shop(Store):
    def __init__(self, name) -> None:
        self.shop_name = name
        super().__init__()
        

shop1 = Shop('apple bd')
shop1.add_product('iPhone', 400, 12)
shop1.add_product('samsunagS22', 350, 20)


shop1.display_product()
shop1.buy_product('iPhone',5)
shop1.display_product()
print(shop1.get_profit())

