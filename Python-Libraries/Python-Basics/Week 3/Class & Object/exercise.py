class Avenger:
    def __init__(self, name, age, gender, superpower, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon

    def get_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSuper Power: {self.superpower}\nWeapon: {self.weapon}"

    def is_leader(self):
        leaders = ["Captain America", "Iron Man"]
        return self.name in leaders

# Create Avengers
avengers = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield"),
    Avenger("Iron Man", 45, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows"),
]

# Display information for each Avenger
for avenger in avengers:
    print(avenger.get_info())
    if avenger.is_leader():
        print(f"{avenger.name} is a leader of the Avengers.")
    print()
