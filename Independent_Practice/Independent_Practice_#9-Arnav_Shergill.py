def dash():
    print("\n-------------------------------------------------------------------------------------------------\n")

def short_dash():
    print("\n--------------------------------------\n")

def section(section_name):
    print(f"--- {section_name} ---\n")

def subsection(subsection_name):
    print(f"-- {subsection_name} --\n")

print("---- Independent Practice #9 ----")

dash()

section("Task 1")

print("It's morphin' time!\n")

# Why couldn't we just move __init__ from the SubClasses to PowerRanger Class and then make instances of PowerRanger instead of making entirely new subClasses?
class PowerRanger:
    def power(self):
        """prints out f-string of color and dino name"""
        return f"color is {self.color} and dino name is {self.dino_name}."

class RedRanger(PowerRanger):
    def __init__(self, color, dino_name):
        """sets the attributes given to the specific instance"""
        self.color = color
        self.dino_name = dino_name
        #takes the attributes from __init__ to use in the f-string in the power method
    def power(self):
        """prints out f-string of color and dino name"""
        return f"color is {self.color} and dino name is {self.dino_name}."

class BlueRanger(PowerRanger):
    def __init__(self, color, dino_name):
        """sets the attributes given to the specific instance"""
        self.color = color
        self.dino_name = dino_name
    def power(self):
        """prints out f-string of color and dino name"""
        return f"color is {self.color} and dino name is {self.dino_name}."

class YellowRanger(PowerRanger):
    def __init__(self, color, dino_name):
        """sets the attributes given to the specific instance"""
        self.color = color
        self.dino_name = dino_name
    def power(self):
        """prints out f-string of color and dino name"""
        return f"color is {self.color} and dino name is {self.dino_name}."

class GreenRanger(PowerRanger):
    def __init__(self, color, dino_name):
        """sets the attributes given to the specific instance"""
        self.color = color
        self.dino_name = dino_name
    def power(self):
        """prints out f-string of color and dino name"""
        return f"color is {self.color} and dino name is {self.dino_name}."

class BlackRanger(PowerRanger):
    def __init__(self, color, dino_name):
        """sets the attributes given to the specific instance"""
        self.color = color
        self.dino_name = dino_name
    def power(self):
        """prints out f-string of color and dino name"""
        return f"color is {self.color} and dino name is {self.dino_name}."

class PinkRanger(PowerRanger):
    def __init__(self, color, dino_name):
        """sets the attributes given to the specific instance"""
        self.color = color
        self.dino_name = dino_name
    def power(self):
        """prints out f-string of color and dino name"""
        return f"color is {self.color} and dino name is {self.dino_name}."

red_ranger = RedRanger("red", "Tyrannosaurus")
blue_ranger = BlueRanger("blue", "Triceratops")
yellow_ranger = YellowRanger("yellow", "Sabertooth Tiger")
green_ranger = GreenRanger("green", "DragonZord")
black_ranger = BlackRanger("black", "Mastodon")
pink_ranger = PinkRanger ("pink", "Pteradactyl")

# put in list so that it's easier to print out the power method for each instance
power_ranger_list = [red_ranger, blue_ranger, yellow_ranger, green_ranger, black_ranger, pink_ranger]

for power_ranger in power_ranger_list:
    print(power_ranger.power())

dash()

section("Task 2")

class Zord:
    def attack(self):
        """prints the attack name"""
        print("Generic Zord attack!")

class TyrannosaurusZord(Zord):
    def attack(self):
        """prints the attack name"""
        print("Tyrannosaurus Zord, Tyranno Slash!")

class TriceratopsZord(Zord):
    def attack(self):
        """prints the attack name"""
        print("Triceratops Zord, Tricera Charge!")

tyranno_zord = TyrannosaurusZord()
tricera_zord = TriceratopsZord()

# put in list so that it's easier to print out the power method for each instance
zord_types = [tyranno_zord, tricera_zord]

for zord in zord_types:
    zord.attack()

dash()
