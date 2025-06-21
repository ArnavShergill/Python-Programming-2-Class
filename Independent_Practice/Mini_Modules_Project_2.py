import formatting as f
import math as m
import random as r
import sys as s
import platform as p

f.title("Mini Project 3: Modules (B)")

f.dash()

f.section("Task 1: Math Functions")

# Some of the results for factorial were too long so extended the string length limit
s.set_int_max_str_digits(100000000)

# Results of different math methods
user_num = float(input("Please input a decimal number: "))
print(f"The rounded up version of {user_num} is {m.ceil(user_num):.2f}")
print(f"The rounded down version of {user_num} is {m.floor(user_num):.2f}")
print(f"The truncated version of {user_num} is {m.trunc(user_num)}")
print(f"The factorial version of {user_num} is {m.factorial(int(user_num))}")
print(f"The square root of {user_num} is {m.sqrt(user_num):.2f}")
print(f"The hypotenuse of a triangle with the sides {user_num} and 15 is {m.hypot(user_num, 15):.2f}")

f.dash()

f.section("Task 2: Random Functions")

#prints the different methods of Random Module
hexadecimal = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
print(f"The random hexadecimal choice is '{r.choice(hexadecimal)}'")
print("The combination of characters in the hexadecimal sample are:")
hexadecimal_sample = r.sample(hexadecimal, k = 5)
for i in hexadecimal_sample:
    print(i)

f.dash()

f.section("Task 3: Platform Information")

# Different methods of Platform Module
print(f"The operating system is {p.system()}")
print(f"The processor is {p.processor()}")
print(f"The python build is {p.python_version()}")

f.dash()

f.section("Task 4: Explore Functions")

# Prints all of the functions/methods from math and platform modules.
print("All of the functions in the Math Module are:")
for i in dir(m):
    print(i)

f.short_dash()

print("All of the functions in the Platform Mudule are:")
for i in dir(p):
    print(i)

f.dash()
