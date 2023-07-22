class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def register_user(self, user):
        self.users.append(user)
        self.total_balance += user.balance

    def get_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return True
        else:
            print("Insufficient balance. Cannot withdraw.")
            return False

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.name}")
            return True
        else:
            print("Insufficient balance. Cannot transfer.")
            return False

    def check_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history


class Customer(User):
    def __init__(self, name, balance, bank):
        super().__init__(name, balance)
        self.bank = bank

    def take_loan(self, amount):
        if amount <= 2 * self.balance and self.bank.loan_feature_enabled:
            self.balance += amount
            self.bank.total_loan_amount += amount
            self.transaction_history.append(f"Took a loan of ${amount}")
            return True
        else:
            print("Loan feature is disabled or loan amount exceeds twice your balance.")
            return False


class Admin(User):
    def __init__(self):
        super().__init__("Admin", 0)
        self.bank = None

    def set_bank(self, bank):
        self.bank = bank

    def create_account(self, name, initial_deposit):
        customer = Customer(name, initial_deposit, self.bank)
        self.bank.register_user(customer)

    def check_total_balance(self):
        return self.bank.get_total_balance()

    def check_total_loan_amount(self):
        return self.bank.get_total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()
        print("Loan feature enabled.")

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()
        print("Loan feature disabled.")


if __name__ == "__main__":
    bank = Bank()
    admin = Admin()
    admin.set_bank(bank)

    admin.create_account("John Doe", 1000)
    admin.create_account("Alice Smith", 500)

    john = bank.get_user_by_name("John Doe")
    alice = bank.get_user_by_name("Alice Smith")

    john.deposit(200)
    john.withdraw(50)

    alice.deposit(100)
    alice.transfer(john, 30)

    admin.enable_loan_feature()
    alice.take_loan(600)
    john.take_loan(1500)

    print(f"John's Balance: ${john.check_balance()}")
    print(f"Alice's Balance: ${alice.check_balance()}")
    print(f"Bank's Total Balance: ${admin.check_total_balance()}")
    print(f"Bank's Total Loan Amount: ${admin.check_total_loan_amount()}")
    print("Transaction History:")
    print(john.get_transaction_history())
    print(alice.get_transaction_history())
