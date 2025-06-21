import formatting as f

f.title("Guided Practie #23")

f.section("Self-Defined Exceptions")

class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("Something went wrong!")
except MyCustomException:
    print("Something went wrong!")

f.dash()

f.section("Self-Defined Exception Examples")

f.subsection("Example 1")

class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        self.message = f"Error: {number} is a negative number."
        super().__init__(self.message)

x = input("Type in a number: ")
x = int(x)

if x < 0:
    try:
        raise NegativeNumberError(x)
    except NegativeNumberError:
        print(f"Error: {x} is a negative number")

f.short_dash()

f.subsection("Example 2")

class FileNotFoundError(Exception):
    def __init__(self, filename):
        self.filename = filename
        self.message = f"Error:{filename} not found"
        super().__init__(self.message)

try:
    with open("alice.txt", "r") as filename:
        print("File opened successfully")
except FileNotFoundError:
    print(f"Error: {filename} not found")

f.dash()