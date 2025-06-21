import formatting as f
import random as r

f.title("Guided Practice #15")

f.section("choice()")

fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi']
random_fruit = r.choice(fruits)
print("The randomly selected fruit is:", random_fruit)

f.dash()

f.section("Choice() Examples")

f.subsection("Example 1")

wwe_wrestlers = ["John Cena", "The Rock", "Stone Cold Steve Austine", "Triple H", "Undertaker"]
random_wwe_wrestler = r.choice(wwe_wrestlers)
print("the randomly selected WWE wrestler is:", random_wwe_wrestler)

f.short_dash()

f.subsection("Example 2")

aew_wrestlers = ["Chris Jericho", "Jon Moxley", "Darby Allin", "Kenny Omega", "Sting"]
random_aew_wrestler = r.choice(aew_wrestlers)
print("The randomly selected AEW wrestler is:", random_aew_wrestler)

f.short_dash()

f.subsection("Example 3")

wwe_wrestlers = ["Austin Tehory", "Brock Lesnar", "Johnny Gargano", "Thomaso Ciampa", "Roman Reigns"]
random_wwe_wrestler_1 = r.choice(wwe_wrestlers)
random_wwe_wrestler_2 = r.choice(wwe_wrestlers)
while random_wwe_wrestler_1 == random_wwe_wrestler_2:
    random_wwe_wrestler_2 = r.choice(wwe_wrestlers)
print("The randomly selected WWE match is between", random_wwe_wrestler_1, "and", random_wwe_wrestler_2)

f.short_dash()

f.subsection("Example 4")

aew_teams = [["Jon Moxley", "Wheeler Yuta", "Cloudio Castagnoli"],["Nick Jackson", "Matt Jackson", "Kenny Omega"], ["Pac", "Penta El Zero Miedo", "Rey Fenix"]]
random_aew_team_1 = r.choice(aew_teams)
random_aew_team_2 = r.choice(aew_teams)
while random_aew_team_2 == random_aew_team_1:
    random_aew_team_2 = r.choice(aew_teams)
print("The randomly selected AEW Trios Tag Team match is between", ", ".join(wrestler for wrestler in random_aew_team_1), "vs", ", ".join(wrestler for wrestler in random_aew_team_2))

f.dash()

f.section("sample")

# Syntax: random.sample(sequence, k)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampled_numbers = r.sample(numbers, 3)

print(sampled_numbers)

f.dash()

f.section("sample() Examples")

f.subsection("Example 1")

weapons = ["Poltergust G-00", "Strobulb", "Dark-Light Device", "Suction Shot"]
random_weapon = r.sample(weapons, k=1)

print(f"The randomly selected weapon is: {random_weapon}")

f.short_dash()

f.subsection("Example 2")

gems = ["Diamond", "Ruby", "Emerald", "Sapphire"]
random_gems = r.sample(gems, 2)

print(random_gems)

f.short_dash()

f.subsection("Example 3")

floors = ["B1", "2F", "5F", "8F", "10F"]
random_floors = r.sample(floors, k = len(floors))

print(random_floors)

f.short_dash()

f.subsection("Example 4")

ghosts = ["Polterkitty", "Goob", "Hammers", "Slinker", "Kruller", "Boos"]
random_ghost = r.sample(ghosts, 1)

print(random_ghost)

f.dash()

f.section("seed()")

r.seed(42)
print(r.random()) #Output: 0.6394267984578837

f.short_dash()

r.seed(42)
print(r.randint(1, 10)) #Output: 2

f.short_dash()

r.seed(1234)
print(r.random()) #Output: 0.1915194503788923

r.seed(5678)
print(r.random()) #Output: 0.8343833162170082

f.dash()
