import formatting as f

# Every section has to use either lambda, filter, and/or map

f.title("Independent Practice #26")

f.dash()

f.section("Lambda Function for Alphabetical Toy Sorting")

# uses lambda and sort to sort the toys
toys = ["Doll", "Car", "Ball", "Kite", "Robot", "Puzzle", "Train", "Boat", "Drum"]
sorted_toys = lambda x: sorted(x)

print(sorted_toys(toys))

f.dash()

f.section("Map Function with Barney & Friends' Ages")

# Adds one to each age value
char_age = {"Barney": 5, "Baby Bop": 3, "BJ": 7, "Riff": 6}

larger_age = list(map(lambda age: age + 1, char_age.values()))

print(char_age)
print(larger_age)

f.dash()

f.section("Filter Function to Find Ripe Apples for Baby Bop")

# filters the numbers over 100 and puts them in another list
weights = [120, 150, 80, 130, 170, 90]

ripe_apples = list(filter(lambda x: x >= 100, weights))

print(weights)
print(ripe_apples)

f.dash()

f.section("Barney & Friends' Alumni")

# puts each kids' name in lowercase and then checks whether or not it is 12 characters long.
barney_kids = ["Selena", "Demi", "Madison", "Debby", "Sarah", "Michael", "Amy", "Katie", "Brandon", "Justin", "Emily", "Jason", "Amanda", "Stephanie"]

lowercase_names = list(map(lambda x: x.lower(), barney_kids))
long_names = list(filter(lambda x: len(x) > 12, lowercase_names))

print(", ".join(barney_kids))
print(", ".join(lowercase_names))
print(", ".join(long_names))

f.dash()
