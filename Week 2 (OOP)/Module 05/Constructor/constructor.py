class Phone:
    manufactured = 'China'
    def __init__(self, owner, brand, price):
        self.woner = owner
        self.brand = brand
        self.price = price
    
    def sand_sms(self, phone, sms):
        text = f'sand to : {phone} {sms}'
        print(text)

my_phone = Phone('Al Amin', 'Sumsang', 21000)
my_phone.sand_sms(893475,'Hello')
print(my_phone.woner, my_phone.brand, my_phone.price)