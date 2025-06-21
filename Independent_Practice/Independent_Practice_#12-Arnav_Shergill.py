import formatting as f
import math as m

f.title("Independent Practice #12")

f.dash()

f.section("Shoryuken!!!!")

ryu_attack = 50
guile_defense = 20

# The instructions weren't clear on where the variables had to be located
# so I accidentally put them in the function instead of outside of them
# and didn't know what to do after I did that. I asked for help, then realized how stupid
# I was to realize the silly mistake I did

def calculate_damage(attack_power, defense_power):
    """figures out the ceiling value for total damage done"""
    damage = m.ceil(attack_power/defense_power)
    return damage

print("Damage Dealt:\n", calculate_damage(ryu_attack, guile_defense)) # Result is 3

f.dash()

f.section("Gravity")

gravity = 9.8
time = 3

# made sure to not make the same mistake as last time

def calculate_jump_height(gravity, time):
    """finds the floor value for the height of the jump given the gravity strength and the time"""
    height = m.floor((gravity * time**2)/2)
    return f"The character jumped a height of {height}"

print(calculate_jump_height(gravity, time)) # Result is 44

f.dash()

f.section("Ken is a Clone")

class Character:
    def __init__(self, name, health, attack_power, defense_power):
        """sets attributes for instance"""
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, enemy_name):
        """calculates and returns the value for damage dealt to enemy"""
        damage_dealt = calculate_damage(self.attack_power, enemy_name.defense_power)
        enemy_name.health = enemy_name.health - damage_dealt
        output = f"enemy's health left:\n{enemy_name.health}"
        return output

ryu = Character("Ryu", 100, 30, 30)
ken = Character("Ken", 100, 25, 25)

print(ryu.attack(ken))

f.dash()
