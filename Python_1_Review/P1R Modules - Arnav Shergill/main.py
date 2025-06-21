import formatting as f
import my_module as m

f.title("Python 1 Review: Modules")

f.dash()

f.section("Storing Function in Modules")

# I used m as the alias for my_module because it was easier and faster to type
name = "Arnav"
print(m.greet(name))

f.dash()

f.section("Importing Entire Modules or Specific Functions")

# imported my_module again for the sake of the instructions
import my_module
print(my_module.greet(name))

#imported the greet function just to complete the instructions and to prove that I can do it
from my_module import greet
print(greet(name))

f.dash()

f.section("Alias")

#used mm as the alias because I couldn't think of a better one than the one given in the example in the instructions
import my_module as mm
print(mm.greet(name))

f.dash()

f.section("Math Module and Functions")

import math

#used a variable because it was simple to write the print statement that way
square_root = math.sqrt(25)
print(square_root)

f.dash()

f.section("Rounding Numbers")

# decided to use pi because of it's length
decimal = 3.141592653589793238462643383279502884197169399375105820
decimal = round(decimal, 2)
print(decimal)

f.dash()

f.section("Random Integers, Choice, & Shuffle")

import random as r

integer = r.randint(1, 10)
print(integer)

random_elements = []
counter = 0
# did the while loop instead of typing out all of the elements because I'm lazy
while counter < 100000:
  random_elements.append(counter)
  counter += 1

print(r.choice(random_elements))

shuffled_elements = []
counter = 0

# same as the previous while loop but with a different number to diffrentiate the two while loops
while counter < 9999:
  shuffled_elements.append(counter)
  counter += 1

#didn't print out as a list because I thought this would look better
r.shuffle(shuffled_elements)
for n in shuffled_elements:
  print(n)

f.dash()

f.section("Datetime Module, Date, and Math Module")

import datetime as dt

current_date = dt.datetime.now()
print(current_date)

# I forgot how to do this, so I had to search it up and learn online.
time_span = dt.timedelta(days=1, hours=12, minutes=30)
print(current_date + time_span)

f.dash()

f.section("Exception Errors")

# I did ZeroDivisionError because that is the error that arises when trying to divide by zero
try:
  print(10/0)
except ZeroDivisionError:
  print("You can't divide by zero!")
else:
  print(10/2)
f.dash()