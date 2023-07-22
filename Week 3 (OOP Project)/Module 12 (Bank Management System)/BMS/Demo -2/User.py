from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.transaction_history = []

    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def transfer(self, recipient, amount):
        pass

    @abstractmethod
    def take_loan(self, amount):
        pass

    def get_transaction_history(self):
        return self.transaction_history

    def authenticate(self, email, password):
        return self.email == email and self.password == password


class Customer(User):
    def create_account(self):
        print(f"Customer {self.name} with email {self.email} has created an account.")

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

    def check_balance(self):
        return self.balance

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.name}")
            return True
        else:
            print("Insufficient balance. Cannot transfer.")
            return False

    def take_loan(self, amount):
        if amount <= 2 * self.balance:
            self.balance += amount
            self.transaction_history.append(f"Took a loan of ${amount}")
            return True
        else:
            print("Loan amount exceeds twice your balance.")
            return False


class Admin(User):
    def create_account(self):
        print(f"Admin {self.name} with email {self.email} has created an account.")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount} as an Admin.")

    def withdraw(self, amount):
        print("Admin cannot withdraw money.")

    def check_balance(self):
        return self.balance

    def transfer(self, recipient, amount):
        print("Admin cannot transfer money.")

    def take_loan(self, amount):
        print("Admin cannot take a loan.")


class Bank:
    def __init__(self):
        self.users = []
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def register_user(self, user):
        self.users.append(user)

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_total_balance(self):
        total_balance = sum(user.check_balance() for user in self.users)
        return total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False


def create_account(bank):
    print("\n--- Create an Account ---")
    print("1. Create Customer Account")
    print("2. Create Admin Account")
    print("3. Back")
    account_choice = int(input("Enter your choice: "))

    if account_choice == 1:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        customer = Customer(name, email, password)
        bank.register_user(customer)
        customer.create_account()
        print("Customer account created successfully.")
    elif account_choice == 2:
        name = input("Enter admin name: ")
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")
        admin = Admin(name, email, password)
        bank.register_user(admin)
        admin.create_account()
        print("Admin account created successfully.")
    elif account_choice == 3:
        pass
    else:
        print("Invalid choice. Please try again.")


def login(bank):
    while True:
        print("\n--- Login ---")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Back")
        login_choice = int(input("Enter your choice: "))

        if login_choice == 1:
            email = input("Enter admin email: ")
            password = input("Enter admin password: ")
            admin = bank.get_user_by_email(email)
            if admin and admin.authenticate(email, password):
                print("Admin logged in successfully.")
                admin_menu(bank)
                break
            else:
                print("Invalid email or password.")
        elif login_choice == 2:
            email = input("Enter customer email: ")
            password = input("Enter customer password: ")
            customer = bank.get_user_by_email(email)
            if customer and customer.authenticate(email, password):
                print(f"Customer {customer.name} logged in successfully.")
                customer_menu(customer, bank)
                break
            else:
                print("Invalid email or password.")
        elif login_choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


def admin_menu(bank):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Create Account")
        print("2. Check Total Balance")
        print("3. Check Total Loan Amount")
        print("4. Toggle Loan Feature (On/Off)")
        print("5. Logout")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account(bank)
        elif choice == 2:
            total_balance = bank.get_total_balance()
            print(f"Total Bank Balance: ${total_balance}")
        elif choice == 3:
            total_loan_amount = bank.get_total_loan_amount()
            print(f"Total Loan Amount: ${total_loan_amount}")
        elif choice == 4:
            loan_feature_enabled = input("Enable or Disable Loan Feature (y/n): ")
            if loan_feature_enabled.lower() == 'y':
                bank.enable_loan_feature()
                print("Loan Feature Enabled.")
            else:
                bank.disable_loan_feature()
                print("Loan Feature Disabled.")
        elif choice == 5:
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


def customer_menu(customer, bank):
    while True:
        print("\n--- Customer Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Take Loan")
        print("6. View Transaction History")
        print("7. Logout")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            customer.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            customer.withdraw(amount)
        elif choice == 3:
            balance = customer.check_balance()
            print(f"Your Account Balance: ${balance}")
        elif choice == 4:
            recipient_email = input("Enter recipient's email: ")
            recipient = bank.get_user_by_email(recipient_email)
            if recipient:
                amount = float(input("Enter the amount to transfer: "))
                customer.transfer(recipient, amount)
            else:
                print("Recipient not found.")
        elif choice == 5:
            amount = float(input("Enter the loan amount: "))
            customer.take_loan(amount)
        elif choice == 6:
            print("Transaction History:")
            for entry in customer.get_transaction_history():
                print(entry)
        elif choice == 7:
            print(f"Customer {customer.name} logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    bank = Bank()
    
    while True:
        print("\n--- Banking Management System ---")
        print("1. Create an Account")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account(bank)
        elif choice == 2:
            login(bank)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
