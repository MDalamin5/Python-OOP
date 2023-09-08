class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.maxWithdrow = 50000
        self.minWithdeow = 500

    def get_balamce(self):
        return self.balance
    
    def deposit(self, amount):
        if amount>0 :
            self.balance +=amount
    
    def withdrow(self,amount):
        if amount <self.minWithdeow:
            print(f'You can not withdeow {amount} taka you have to minumum withdrow {self.minWithdeow}')
        elif amount > self.maxWithdrow:
            print(f'You have to follow goverment rule you can not withdrow more then {self.maxWithdrow}')
        elif amount>=self.balance:
            print(f'Fokir bata tor accoutn a ato taka ni aga taka deposite kor tor account a acha {self.balance}')
        else:
            self.balance -= amount
            print(f'Here is your money: {amount}')
            print(f'Taka withdrow sussfully you left amount {self.balance}')


brac = Bank(50000)
print(brac.get_balamce())
brac.withdrow(50)
brac.withdrow(3453452)
brac.withdrow(3453)

dbbl = Bank(3453245)
dbbl.withdrow(2345)