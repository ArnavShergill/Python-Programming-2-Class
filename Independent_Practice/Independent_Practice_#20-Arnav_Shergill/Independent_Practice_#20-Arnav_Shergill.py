import formatting as f

f.title("Independent Practice #20")

f.dash()

f.section("Addition")

# Does addition unless incorrect input was given
try:
    num1 = int(input("Input number 1: "))
    num2 = int(input("Input number 2: "))
    result = num1 +num2
except ValueError:
    print("These are not integers! shame on you.")
else:
    print("\n", result)

f.dash()

f.section("Addition Calculator")

# does same as addition but loops to start so that user can retype correct input
while True:
    try:
        num1 = int(input("Input number 1: "))
        num2 = int(input("Input number 2: "))
        result = num1 + num2
    except ValueError:
        print("Make sure that you are inputting an integer!")
        continue
    else:
        print("\n", result)
        break

f.dash()

f.section("Cats & Dogs")

# Writes new files, then reads from them. says if file is not found if file is not found
while True:
    with open("cats.txt", "w") as file:
        file.write("Sir Meowsalot\n")
        file.write("King Julius\n")
        file.write("Queen Cleopatra")

    with open("dogs.txt", 'w') as file:
        file.write("Brian Griffin\n")
        file.write("Captain Woofs\n")
        file.write("Scooby Doo")

    try:
        with open("cats.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print("This file was not found!")

    try:
        with open("dogs.txt", "r") as file:
            f.short_dash()
            lines = file.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print("This file was not found!")
    break

f.dash()

f.section("Silent Cats & Dogs")

# same as cats and dogs but doesn't say that it fails if it does
while True:
    with open("cats.txt", "w") as file:
        file.write("Sir Meowsalot\n")
        file.write("King Julius\n")
        file.write("Queen Cleopatra")

    with open("dogs.txt", 'w') as file:
        file.write("Brian Griffin\n")
        file.write("Captain Woofs\n")
        file.write("Scooby Doo")

    try:
        with open("cats.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        pass

    try:
        with open("dogs.txt", "r") as file:
            f.short_dash()
            lines = file.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        pass
    break

f.dash()

f.section("Common Words")

# counts the number of times the word "the" shows up in the story
with open("TheLongestJourney.txt", encoding = "utf-8") as file:
    lines = file.readlines()
    counter = 0
    for line in lines:
        line_count = line.lower().count("the")
        counter = counter + line_count

print("The amount of times the word 'the' is in the book 'The Longest Journey' is: ", counter)

f.dash()
