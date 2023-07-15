class Shopping:
    cart = []
    def __init__(self,name, location) -> None:
        self.name = 'JFP'
        self.location = 'Near Bashundhara'
        pass

    def purchase(self, item, pirce, amount):
        remaining  = amount - pirce
        print(f'buying : {item}, for price: {pirce}, remain amount: {remaining}')

    @staticmethod
    def static_method(a,b):
        result = a+b
        print (result)
    
    @classmethod
    def class_method(self, name, location):
        print(f'Jomuna geacelm {name}, kinta ar {location} a dam base')



Shopping.static_method(3,4)

jft = Shopping('Jomuna', 'Bashundhara')

jft.class_method('Jomuna','Bashundhar')
Shopping.class_method('jk','kad')
jft.static_method(34,34)
