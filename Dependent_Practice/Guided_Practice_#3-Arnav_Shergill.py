import formatting as f

f.title("Guided Practice #3")

f.dash()

f.section("Filling a Dictionary with User Input")

responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ").strip().title()
    response = input("Which mountain would you like to climb someday? ").strip()

    #Store the response in the dictionary.
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ").strip().lower()
    if repeat == "no":
        polling_active = False
        break

print("\n- Poll results -\n")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

f.dash()

f.section("Looping Through a Dictionary")

f.subsection("Looping Through All Key-Value Pair")

print("- Loops -\n")

user_0 = {"username":"chefsushi", "first":"sushanth", "last":"yarlagadda"}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("- Favorite Languages -\n")

favorite_languages = {"jen":"python","sarah":"c","edward":"ruby","phil":"python"}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

f.dash()

f.section("Looping though All the Keys in a Dictionary")

f.subsection("All The Keys")

favorite_languages = {"jen":"python","sarah":"c","edward":"ruby","phil":"python"}

for name in favorite_languages.keys():
    print(name.title())

f.short_dash()

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("\n")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

f.dash()

f.section("Looping Throug ha Dictionary's Keys in a Particular Order")

f.subsection("Particular Order")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking th poll.")

f.dash()

f.section("Looping Through All Values in a Dictionary")

f.subsection("All Section")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for langauge in set(favorite_languages.values()):
    print(langauge.title())

f.dash()
