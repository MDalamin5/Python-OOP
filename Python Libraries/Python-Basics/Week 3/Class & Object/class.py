import datetime as dt

class CricketPlayer:
    def __init__(self,fname, lname, dob, team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = dob
        self.team = team
        self.scores = []

    def get_age(self):
        now = dt.datetime.now()
        return now.year - self.birth_year
    
    def add_score(self, score):
        self.scores.append(score)

    def get_avgScore(self):
        return sum(self.scores) / len(self.scores)
    
    

    def __gt__(self, other):
        return self.get_avgScore() > other.get_avgScore()
        
        
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} is from {self.team} Team'
    



virat = CricketPlayer('Virat', 'Koli', 1988, 'INDIA')
alamin = CricketPlayer('Md', 'Al Amin', 1997, 'Bangladesh')
print(virat.team)
# print(virat.get_age())
virat.add_score(50)
virat.add_score(40)
virat.add_score(80)
virat.add_score(30)
# print(virat.get_avgScore())
alamin.add_score(30)
alamin.add_score(40)
alamin.add_score(70)
alamin.add_score(90)
# print(alamin.get_avgScore())

print(alamin > virat)
print(alamin)
