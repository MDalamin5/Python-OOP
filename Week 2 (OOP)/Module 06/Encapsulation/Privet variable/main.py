class Bank:
    def __init__(self, holder_name, initial_Deposite) -> None:
        self.holder_name = holder_name
        self.__balance = initial_Deposite

    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance (self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount>self.__balance:
            print('Your balance is low First deposte some amount')
        else:
            print(f'{amount} Taka withdraw sussfully')
            print('Thank You for choosing Us')

Rafsan = Bank('Choto Bro', 5000)
# print(Rafsan.__balance)
Rafsan.deposite(34534)
print(Rafsan.get_balance())
Rafsan.withdraw(3454)
# print(dir(Rafsan))
print(Rafsan._Bank__balance)

# enceplution