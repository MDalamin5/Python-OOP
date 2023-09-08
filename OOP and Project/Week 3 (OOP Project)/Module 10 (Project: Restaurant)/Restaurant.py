# *******************
class Restaurant:
    def __init__(self, name, rent, menu =[]) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.profit = 0
        self.balance = 0
        

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee
    
    def add_order(self, order):
        self.orders.append(order)

    
    def recive_payment(self,order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not Enouth Money. Pay more')
        

    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f"Expense {amount} for {description}")

        else:
            print(f'Not enough Money to pay {amount}')

    def pay_salary(self, employee):
        print(f'Paying Salary for {employee.name}, Salary: {employee.salary}')
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()

    def show_employees(self):
        print(f'=============SHOWING EMPLOYEE================')
        if self.chef is not None:
            print(f"Chef: {self.chef.name} with salary: {self.chef.salary}")
        print('*'*45)
        if self.server is not None:
            print(f"Server: {self.server.name} with salary {self.server.salary} ")
        print('*'*45)
        if self.manager is not None:
            print(f"Manager: {self.manager.name} with salary {self.manager.salary}")
        print('='*45)
