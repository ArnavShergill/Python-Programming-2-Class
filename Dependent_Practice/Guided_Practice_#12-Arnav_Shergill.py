import formatting as f

f.title("Guided Practice #12")

f.dash()

f.section("The Python Standard Library")

from random import randint

x = randint(1, 6)

from random import choice

players = ('Charles', "Martina", "Michael", "Florence", "Eli")
first_up = choice(players)
print("Your up first,", first_up)

f.dash()

f.section("Math Module")

import math

f.subsection("Ceil()")

print(math.ceil(3.2)) #Output: 4
print(math.ceil(3.7)) #Output: 4
print(math.ceil(4)) #Output: 4

f.short_dash()

f.subsection("Floor()")

print(math.floor(3.2)) #Output: 3
print(math.floor(3.7)) #Output: 3
print(math.floor(4)) #Output: 4

f.short_dash()

f.subsection("Trunc()")

print(math.floor(3.2)) #Output: 3
print(math.floor(3.7)) #Output: 3
print(math.floor(4)) #Output: 4

f.short_dash()

f.subsection("Hypot()")

print(math.hypot(3, 4)) #Output: 5.0
print(math.hypot(5, 12)) #Output: 13.0

f.short_dash()

f.subsection("sqrt()")

print(math.sqrt(9)) #Output: 3.0
print(math.sqrt(16)) #Output: 4.0

f.short_dash()

f.subsection("Other Examples")

# Calculate the square root of 9
print(math.sqrt(9)) #Output: 3.0

#Calculate the sine of pi/2
print(math.sin(math.pi/2)) #Output: 1.0

f.dash()

f.section("ceil()")

f.subsection("Lists/Tuples")

my_list = [2.5, 3.7, 4.2, 5.9]
my_tuple = (1.3, 2.7, 3.1, 4.5)

# Use ceil() with lists
for number in my_list:
    print(math.ceil(number)) #Output: 3, 4, 5, 6

for number in my_tuple:
    print(math.ceil(number)) #Output: 2, 3, 4, 5

f.short_dash()

f.subsection("Dictionaries")

my_dict = {'a':2.5, 'b':3.7, 'c':4.2, 'd':5.9}

#Use ceil() with dictionaries
for key in my_dict:
    print(key, math. ceil(my_dict[key])) #Output: a 3 b 4 c 5 d 6

f.short_dash()

f.subsection("Functions")

def calculate_total_cost(cost_per_unit, quantity):
    total_cost = cost_per_unit * quantity
    return math.ceil(total_cost)

print(calculate_total_cost(2.5, 3)) #Output: 8

f.short_dash()

f.subsection("Classes")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_required_paint(self, paint_coverage):
        total_area = self.calculate_area()
        return math.ceil(total_area/paint_coverage)

my_rectangle = Rectangle(5, 3)

print(my_rectangle.calculate_required_paint(10)) #Output: 2

f.short_dash()

f.subsection("Strings")

my_string = "Python is a great language"

#use ceil() with strings
num_of_chars = len(my_string)
num_of_pages = math.ceil(num_of_chars / 20) #Assuming 20 characters per page
print("Number of pages required:", num_of_pages) #Output: Number of pages required: 2

f.short_dash()

f.subsection("If Statements & Loops")

# Use ceil() with if statements and loops
for i in range(10):
    if math.ceil(i/2) >= 3:
        print(i) # Output: 5, 6, 7, 8, 9

f.dash()

f.section("floor()")

f.subsection("Lists/Tuples")

numbers = [3.14, 5.9, 6.8, 7.2, 10.1]
floors = [math.floor(n) for n in numbers]
print(floors) #Output: 3, 5, 6, 7, 10

f.short_dash()

f.subsection("Dictionaries")

prices = {'apple': 2.99, 'banana': 1.49, 'orange': 1.99}
floor_prices = {k: math.floor(v) for k, v in prices.items()}
print(floor_prices) # Output: {'apple': 2, 'banana': 1, 'orange': 1}

f.short_dash()

f.subsection("Functions")

def calculate_total_cost(price, quantity):
    total = price * quantity
    return math.floor(total)

cost = calculate_total_cost(2.99, 3)
print(cost) #Output: 8

f.short_dash()

f.subsection("Classes")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self. height = height

    def area(self):
        return self.width * self.height

    def rounded_area(self):
        return math.floor(self.area())

rect = Rectangle(3.5, 2.25)
print(rect.area())
print(rect.rounded_area())

f.short_dash()

f.subsection("Strings")

string= "Hello, World!"
num_chars = len(string)
num_chunks = math.floor(num_chars/5)
chunks = [string[i:i+5] for i in range(0, num_chars, 5)]
print(num_chars) #Output: 13
print(num_chunks) #Output: 2
print(chunks) #Output: ['hello', ',worl', 'd!']

f.dash()
