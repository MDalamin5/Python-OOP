def call():
    print('Calling someone i don\'t know')
    return 'call done'

class Phone:
    price = 19000
    color = 'blue'
    brand = 'sumsung'
    features = ['Camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')
    def sand_message(self, phone, sms):
        text = f'Seanding SMS to : {phone} and message: {sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
text = my_phone.sand_message('01641876457', 'Hello boss')
print(text)