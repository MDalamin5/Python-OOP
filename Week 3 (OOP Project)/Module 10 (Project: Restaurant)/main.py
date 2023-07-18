from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Customer, Server, Manager

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to menu

    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)


    # add drinks to the menu

    cock = Drinks('Cock', 50, True)
    menu.add_menu_item('drinks', cock)
    coffee = Drinks('Mocha', 300, False)
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
    





# call the main method
if __name__ == '__main__':
    main()