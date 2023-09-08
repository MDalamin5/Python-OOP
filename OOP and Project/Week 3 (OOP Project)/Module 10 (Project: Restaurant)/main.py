from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Customer, Server, Manager
from Order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to menu

    burger_1 = Burger('Naga Burger', 2000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)


    # add drinks to the menu

    cock = Drinks('Cock', 300, True)
    menu.add_menu_item('drinks', cock)
    coffee = Drinks('Mocha', 600, False)
    menu.add_menu_item('drinks', coffee)

    menu.show_menu()

    restaurant = Restaurant('Pagla Baba Restaurant', 2000, menu)
    manager = Manager('Kala Chan Manager', '0164199999', 'kala@chan.com', 'Komla-Pur', 1500, 'Jan 06 2022', 'core')
    restaurant.add_employee('manager', manager)
    chef = Chef('Rustom Baburchi', '01389474234', 'rustom@kopa.com', 'Puran Dhaka', 500, 'Jun 01 2022', 'Chafe', 'chicken Rost' )
    restaurant.add_employee('chef', chef)
    server = Server('Chotu server', '0184385745', 'chotu@server.com', 'Restaurant', 200, 'March 01 2023', 'server')
    restaurant.add_employee('server', server)

    # show employee
    restaurant.show_employees()

    # customer-1 
    customer_1 = Customer('Niloy Ahmed', '0182345453', 'niloy@nsu.edu', 'Bashundhara', 10000)
    order_1 = Order(customer_1, [pizza_3, coffee, pizza_2, pizza_1, cock])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # Customer one paying for order-1
    restaurant.recive_payment(order_1, 8000, customer_1)
    print(f"Current Revenue after first Customer: {restaurant.revenue}\nCurrent Balance after first Customer: {restaurant.balance}")
    print('`'*45)

        # customer -2
    customer_2 = Customer('Aminul Islam', '01824545453', 'aminul@nsu.edu', 'Bashundhara', 50000)
    order_2 = Order(customer_2, [pizza_1,  burger_2, coffee, cock, burger_1, pizza_2])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    # Customer one paying for order-1
    restaurant.recive_payment(order_2, 9000, customer_2)

    print(f"Current Revenue after first Customer: {restaurant.revenue}\nCurrent Balance after first Customer: {restaurant.balance}")
    print('`'*45)

    # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('After paying Rent: ', restaurant.revenue, restaurant.balance, restaurant.expense)
    print('`'*45)
    # pay Salary
    restaurant.pay_salary(chef)
    print('After paying Salary: ', restaurant.revenue, restaurant.balance, restaurant.expense)

 

# call the main method
if __name__ == '__main__':
    main()