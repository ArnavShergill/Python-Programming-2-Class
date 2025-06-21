import formatting as f

f.title("Independent Practice #4")

f.section("Task 1 - People")

#Made a list for some of the values so that there is multiple elements
Person_1 = {"Name":"Arnav", "Age":17, "Grade":11, "Favorite Subject":"Python Programming 2 Honors", "Extracurriculars":["Mountain Biking", "Volunteering"], "GPA":3.6, "Hobbies":["Gaming", "Photography"]}
Person_2 = {"Name":"Mahee", "Age":15, "Grade":11, "Favorite Subject":"Culinary","Extracurriculars":["Being a Chill Guy", "Rizzing up the Homies"], "GPA":1.4, "Hobbies":["Doomscrolling on Instagram Reels", "Drinking the Grimace Shake"]}
Person_3 = {"Name":"Amshul", "Age":16, "Grade":11, "Favorite Subject":"Math 1 Honors", "Extracurriculars":["Acting tough", "volunteering"], "GPA":0.5, "Hobbies":["Fortnite Dances", "Barely Passing Classes"]}

People = [Person_1, Person_2, Person_3]

print("- Looping Through People's Information -\n")

#used two loops so that there is a nested loop involved
for user_info in People:
    for value in user_info.values():
        print(value)

print("\n- Checking if Cassandra is in the list -\n")

#checks the name of the person using keys.
for user_info in People:
        if user_info["Name"] != "Cassandra":
            print("Cassandra is not in the databases")

print("\n- Checking People's GPA -\n")

#Uses keys to find the value of people's GPA
for user_info in People:
    print(user_info['GPA'])

f.dash()

f.section("Task 2 - Pets")

print("- Looping through Pet Information -\n")

#dictionaries
Pet_1 = {"animal":"bunny", "owner":"mahee", "age":6,"color":"black", "favorite toy":"doll", "vaccinated":False, "weight":5, "microchipped":True}
Pet_2 = {"animal":"cat", "owner":"amshul", "age":12,"color":"brown", "favorite toy":"back scratcher", "vaccinated":True, "weight":12, "microchipped":False}
Pet_3 = {"animal":"dog", "owner":"Arnav", "age":8,"color":"brown", "favorite toy":"squeaky toy", "vaccinated":True, "weight":24, "microchipped":True}

#strangely had problems with Pets being a dictionary so had to become list
Pets = [Pet_1, Pet_2, Pet_3]

#loop so that it goes through all of the key and values
for pet in Pets:
    print(pet)

f.short_dash()

print("- Modifying a Value in a Dictionary -\n")

#used key to change value because it's straightforward and easy
Pet_1["vaccinated"] = True
print(Pet_1)

f.short_dash()

print("- Who are the Owners? -\n")

for pet in Pets:
    print(pet["owner"].title())

f.dash()
