class Player:
    def __init__(self, fname, lname, dob) -> None:
        self.first_name = fname
        self.last_name = lname
        self.birth_day = dob


    def display(self):
         print(f'Name: {self.first_name} {self.last_name} DOB: {self.birth_day}')
    

class FootballPlayer(Player):
    def __init__(self, fname, lname, dob, team) -> None:
        self.team = team
        super().__init__(fname, lname, dob)


alamin = FootballPlayer('MD', 'Al Amin', 1999, 'Bangladesh')
alamin.display()
