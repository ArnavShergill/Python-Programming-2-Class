import formatting as f

f.title("Independent Paractice #3")

f.dash()

f.section("Task 1 - Glossary 2")

glossary = {}

print("- Printing Values -\n")

#toyota is key and supra is value
glossary["Toyota"] = "Supra"

print(f"Toyota: {glossary.get('Toyota')}")

#used curly braces inside the parenthesis so that BRZ and Subaru can be linked as key and value
glossary.update({"Subaru":"BRZ"})

print(f"Subaru: {glossary.get('Subaru')}")

print("\n- Looping, Inputing, and Outputing -\n")

#did while loop instead of letting user print quit because writing the code for it was easier.
counter = 0
while counter < 5:
    user_input = input("Enter a Car Model then Make seperated with a colon: ")
    key, value = user_input.split(":")
    glossary[key] = value
    counter += 1

# used for loop since it was easier and user can see what value was associated with what key
print(glossary)
for key in glossary:
    print(f"{key}")
    print(f"{glossary[key]}\n")

f.dash()

f.section("Task 2 - Rivers")

Major_Rivers = {"egypt":"nile", "united states":"mississipi", "brazil":"amazon"}

#prints the river and country in f-string
for key in Major_Rivers:
    print(f"The {Major_Rivers[key].title()} runs through {key.title()}")

#prints the names of rivers in a for loop and numbers them, which is what n is for
print("\nThe names of the rivers are:")
n = 0
for river in sorted(Major_Rivers):
    n += 1
    print(f"{n}) {Major_Rivers[river].title()}")

print()

#same concept with rivers, but instead is with the countries that the rivers are in.
print("\nThe names of the countries are:")
n = 0
for country in sorted(Major_Rivers.keys()):
    n += 1
    print(f"{n}) {country.title()}")

f.dash()

f.section("Task 3 - Polling")

#people who took the poll
favorite_languages = {"jen":"python","sarah":"c","edward":"ruby","phil":"python"}

#people who should take the toll
should_take_toll = ("jen", "sarah", "edawrd", "phil", "alex", "bartholemew", "jamal", "jeremy", "richard", "james")

#filters through which person did the toll or not and printed that the person should do the poll for the people who didn't do the poll and prints congrats for the people who did the poll
for name in sorted(should_take_toll):
    if name not in favorite_languages:
        print(f"{name.title()} needs to take the poll.")
    else:
        print(f"Thanks {name.title()} for taking the poll!")

f.dash()
