import formatting as f

f.title("Guided Practice #21")

f.dash()

f.section("Exceptinos Syntax")

try:
    file = open("my_file.txt", "w")
    try:
        file.write("Writiong some data to the file")
    finally:
        file.close()
except IOError:
    print("Error: my_file.txt does not excist or it can't be opened for output.")

f.dash()

f.section("Finally")

try:
    #some code that may raise an exception
    print("Executing some code in try block")
except:
    #handle the exception
    print("An exception occurred")
finally:
    #ocd that should always execute, regardless of whether an exception was raised or not
    print("Finally block executed")

f.short_dash()

f.subsection("Example with Division by Zero")

while True:
    try:
        print("\nPlease enter two numbers in the prompts below to try out division. Type in 'q' to quit")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print("Result: ", result)
        if num1 == 'q':
            break
        elif num2 == 'q':
            break
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        break
    finally:
        print("Finally block executed")
        break

f.short_dash()

f.subsection("Example with File Handling")

try:
    file = open("example.txt", 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
    print("Finally block excecuted")

f.dash()

f.section("Raise Exceptions")

f.subsection("Raise a Built-In Exception")

try:
    raise TypeError("Invalid argument")
except TypeError:
    print("Invalid Argument")

f.short_dash()

f.subsection("Riase a Custom Exception")

class CustomException(Exception):
    pass

try:
    raise CustomException("Something went wrong")
except CustomException:
    print("something went wrong")

f.short_dash()

f.subsection("More Examples to Try")

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as ve:
    print(ve)

f.short_dash()

f.subsection("Exception with Files")

try:
    file = open("myfile.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError as fnfe:
    print(fnfe)

f.dash()

f.section("Using Raise with Loops")

my_list = [1, 2, 3, 4, 5]
try:
    for num in my_list:
        if num > 3:
            raise ValueError("Number greater than 3 found in list!")
except ValueError:
    print("Number greater than 3 found in list!")

x = 10
while x > 0:
    if x == 5:
        try:
            raise ValueError("Number equals 5, stopping loop!")
        except ValueError:
            print("Number equals 5, stopping loop!")
    print(x)
    x -= 1

f.dash()

f.section("Using Raise in functions & Classes")

def power_level(name, level):
    if level < 0:
        try:
            raise ValueError("Power level cannot be negative!")
        except ValueError:
            print("Power level cannot be negative!")
    print(f"{name}'s power level is {level}")

# Testing the function
power_level("Goku", 9000)
power_level("Vegeta", -8000) #This will riase ValueError

f.dash()

f.section("Raise with Lists & Dictionaries")

def collect_star(star_number, stars_collected):
    if star_number < 1 or star_number > 120:
        try:
            raise ValueError("Invalid star number! Must be between 1 and 120.")
        except ValueError:
            print("Invalid star number! Must be between 1 and 120.")
    # Adjust for zero-based index
    stars_collected[star_number - 1] = True  
    print(f"You collected star number {star_number}!")

# Testing the function
stars = [False] * 120
collect_star(64, stars)
try:
    collect_star(121, stars)
except IndexError:
    print("Star number is out of index.")

f.short_dash()

def use_powerup(powerup, mario_stats):
    if powerup not in mario_stats:
        try:
            raise KeyError(f"Invalid powerup '{powerup}'! Available powerups: {list[mario_stats.keys()]}")
        except KeyError:
            print(f"Invalid powerup '{powerup}'! Available powerups: {list[mario_stats.keys()]}")
    mario_stats[powerup] -= 1
    print(f"Mario used a {powerup} powerup!")

#Testing the function
stats = {
    "coins":30,
    "lives":3,
    "mushrooms":1
}
use_powerup("mushrooms", stats)
try:
    use_powerup("caps", stats) #This will raise a KeyError
except KeyError:
    print("incorrect powerup")

f.short_dash()

