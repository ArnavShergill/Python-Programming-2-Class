import formatting as f
import math as m
import random as r

f.title("Independent Practice #13")

f.dash()

f.section("Program 1")


def factorial_ask():
    """gets the input for the factorial, raises an error if it isn't a number, then prints out the result if all is successful"""
    user_number = int(input("Input a number to calculate a factorial: "))
    pre_calc_num = user_number
    if pre_calc_num < 0:
        raise Exception
    post_calc_num = m.factorial(pre_calc_num)
    print(f"\nThe factorial for {pre_calc_num} is {post_calc_num}")
    
# checks for two instead of one because one error might be caused if input isn't a number nad the other one is for if the input is not positive
while True:
    try:
        factorial_ask()
        break
    except (ValueError, Exception):
        print("\nThis either isn't an integer or it isn't positive. Try again.")
        continue

f.dash()

f.section("Program 2")

class HelloKitty:
    def __init__(self):
        """chooses character randomly out of a list, then asks for the age, if the age isn't a float, then raise an error and loop over again"""
        characters = ["Hello Kitty", "My Melody", "Batz-Maru", "Keroppi", "Chococat"]
        self.character = r.choice(characters)
        self.age = input(f"What is the age for {self.character} as a float?\n")
        while True:
            try:
                self.age = float(self.age)
                break
            except ValueError:
                print("That's not a float! try again.")
                continue

    def print_age(self):
        """returns trunced age in user-friendly manner"""
        return f"\nThe age as a whole number for {self.character} is {m.trunc(self.age)}"

# Three objects and printed out trunced ages
character1 = HelloKitty()
print(character1.print_age())

f.short_dash()

character2 = HelloKitty()
print(character2.print_age())

f.short_dash()

character3 = HelloKitty()
print(character3.print_age())

f.dash()

f.section("Program 3")

#valueerror only appears if input not a float
while True:
    try:
        float_input = float(input("Input a float: "))
        break
    except ValueError:
        print("This isn't a float! Try again.")
        continue

whole_number = m.trunc(float_input)

#modulo because need the remainder to decide whether number is even or odd.

if whole_number % 2 == 0:
    print("\nEven Number!")
else:
    print("\nOdd Number!")

f.dash()
