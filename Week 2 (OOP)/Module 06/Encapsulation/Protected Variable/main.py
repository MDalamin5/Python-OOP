class Bank:
    def __init__(self, holder_name, initial_Deposite) -> None:
        self.holder_name = holder_name # public
        self.__balance = initial_Deposite  #privet
        self._brance_name = 'Bashundhara r/a' # Protected

    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance (self):
        return self.__balance

Rafsan = Bank('Choto Bro', 5000)
# print(Rafsan.__balance)
Rafsan.deposite(34534)
print(Rafsan.get_balance())