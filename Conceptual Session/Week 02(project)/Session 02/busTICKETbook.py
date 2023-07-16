# this poject aboub a bus ticket book using OOP concepts
# Admin
# 1. Add a new bus
# 2. Check available buses
# 3. can check bus info

# USER
# 1 check aviable buses
# 2 can check bus info
# 3 can reserve seat

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        


class Bus:
    def __init__(self, coach, driver, arrival, deaparture, form_des, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.deaparture = deaparture
        self.from_des = form_des
        self.to = to
        self.seat = ['Empty' for i in range(20)]
        pass

# b = Bus(2, 'Rahim', '12 PM', '12:30 PM', 'Dhaka', 'Chittagong')
# # print(b)
# print(vars(b))

class NSU_bus:
    total_bus = 5
    total_bus_list = []

    def add_bus(self):
        bus_no = int(input('Enter the bus Number or Coach No: '))

        flag=1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print('Bus is already Added')
                flag = 0

        if flag:
            bus_driver = input('Enter bus driver: ')
            bus_arrival = input('Enter bus Arrival time: ')
            bus_deprature = input('Enter bus Departure Time: ')
            bus_from = input('Enter bus start Form: ')
            bus_to = input('Enter Bus Destination: ')
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_deprature,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\n Bus added Successfully")


# company = Phitron()
# company.add_bus()

class Counter(NSU_bus):
    user_list = []
    

    def reservation(self):
        bus_no = int(input('Enter bus No: '))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger_name = input('Enter your Full Name: ')
                seat_no = int(input("Enter Your Seat NO: "))
                if seat_no >20:
                    print('No seat are Available!!!')
                elif w['seat'][seat_no-1]!= 'Empty':
                    print('Seat is Already Booked')
                else:
                    w['seat'][seat_no-1] = passenger_name
            else:
                print('No Buses are Available!!!')
        
        # for bus in self.total_bus_list:
        #     print(bus['seat'])
    
    def show_ticket(self):
        bus_no = int(input("Enter bus number: "))

        for w in self.total_bus_list:
            if bus_no == w ['coach']:
                print('*'*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number: {bus_no} \t\t\t Driver Name: {w['driver']}")
                print(f"Arrival : {w['arrival']} \t\t\t Departur Time: {w['deaparture']}")
                print(f"From: \t {w['from_des']} \t\t\t To: \t {w['to']}")
                print()

                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end= "\t")
                        a+=1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end= "\t")
                    print()
                    print('='*50)
    
    def get_users(self):
        return self.user_list
    
    def create_account(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.new_user = User(name, password)
        self.user_list.append(self.new_user)

    
    def available_buses(self):
        if len(self.total_bus_list)==0:
            print("No Buses Avilabale \n")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Bus Number: {bus['coach']} \t Driver: {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t Departure Time: {bus['deaparture']}")
                print(f"From: \t{bus['form_des']} \t\t To: \t {bus['to']}")
                print('*'*50)
    


while True:
    company = NSU_bus()
    b = Counter()
    print("1. Create an Account")
    print("2. Login Account")
    print("3. Exit")

    user_input = int(input("Enter your choice: "))

    if user_input == 3:
        break
    elif user_input == 1:
        b.create_account()
    elif user_input == 2:
        name = input("Enter Your Username: ")
        password = input("Enter Your Password: ")

        flag = 0
        isAdmin = False

        if name =='Al Amin' and password == '1234':
            isAdmin = True

        if isAdmin==False:
            for user in b.get_users():
                if user['username']==name and user['password']==password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10}Welcome to BUS TICKET BOOKING SYSTeM")
                    print("1. Aviailable Buses")
                    print("2. Show Bus Info")
                    print("3. Reservation Ticket")
                    print("4. Exit")



        
                        





















# Global 
#         1. Create an Account
#         2. Login To Your Account
#         3. exit


# Admin:
#     1. add new Bus
#     2. available buses
#     3. can check bus info
#     4. exit

# User: 
#     1. bus info
#     2. reserve/ booking ticket
#     3. available buses
#     4. exit