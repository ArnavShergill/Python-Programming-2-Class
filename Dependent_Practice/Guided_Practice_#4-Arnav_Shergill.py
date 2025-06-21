import formatting as f

f.title("Guided Practice #4")

f.dash()

f.section("A List of Dictionarys")

alien_0 = {'color':"green", "points":5}
alien_1 = {"color":"yellow", "points":10}
alien_2 = {"color":"red", "points":15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print()

#make an empty list for storing aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {"color":"green", "points":5, "speed":"slow"}
    aliens.append(new_alien)

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created
print(f"Total number of aleins: {len(aliens)}")

print()

#make an empty list for storing aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {"color":"green", "points":5, "speed":"slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

print()

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

f.dash()

f.section("List in a Dictionary")

#store information abot a pizza being ordered.

pizza = {'crust':'thick', 'toppings':['mushrooms','extra cheese']}

#summarize the order.
print(f"You ordered a {pizza['crust']} with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

f.short_dash()

f.subsection("Favorite Languages")

favorite_languages = {'jen': ['python', 'ruby'], 'sarah':['c'], 'edward':['ruby','go'], 'phil':['python', 'haskell']}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

f.dash()

f.section("A Dictionary in a Dictionary")

users = {"popcornDave":{"first":"dave","last":"smith","location":"charlotte"}, "princessRhea":{"first":"rhea","last":"kothur","location":"charlotte"}}

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

print(f"\tFull name: {full_name.title()}")
print(f"\tLocation: {location.title()}")

f.dash()
