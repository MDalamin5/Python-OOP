# Ena Poribhob

class Company:
    def __init__(self, name , address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.rute = []
        self.supervisor = []
        self.counter = []
        self.fare = []
        pass

class Driver:
    def __init__(self,name, licence, age, acdient_history, exprence,mob_no) -> None:
        self.name = name
        self.licence = licence
        self.age = age
        self.acdient_history = acdient_history
        self.exprence = exprence
        self.mob_num = mob_no

class Counter:
    def __init__(self,counter_name) -> None:
        self.counter_name = counter_name

    def purchase_a_ticket(self, name, mob_no,strat_des, end_des):
        self.name = name
        self.mob_no = mob_no
        self.start_des = strat_des
        self.end_des = end_des

class Passenger:
    pass

class Supervisor:
    pass
        