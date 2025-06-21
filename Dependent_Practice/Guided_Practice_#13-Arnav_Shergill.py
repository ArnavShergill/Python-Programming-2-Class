import formatting as f
import math as m

f.title("Guided Practice #13")

f.dash()

f.section("Trunc()")

f.subsection("Lists/Tuples")

my_list = [3.14159, 2.71828, 1.61803]
my_list_trunc = [m.trunc(i) for i in my_list]
print(my_list_trunc) #Output: [3, 2, 1]

f.short_dash()

f.subsection("Dictionaries")

my_dict = {"pi":3.14159, "e":2.71828, "phi":1.61803}
my_dict_trunc = {k: m.trunc(v) for k, v in my_dict.items()}
print(my_dict_trunc) #Output: {'pi':3, 'e':2, 'phi':1}

f.short_dash()

f.subsection("Classes")

class MyMath:
    def __init__(self, x):
        self.x = x

    def trunc(self):
        return m.trunc(self.x)

my_obj = MyMath(3.14159)
print(my_obj.trunc()) #Output: 3

f.short_dash()

f.subsection("Strings")

my_str = "3.14159"
my_str_trunc = str(m.trunc(float(my_str)))
print(my_str_trunc)

f.short_dash()

f.subsection("Booleans")

my_bool = (m.trunc(3.14159) == 3)
print(my_bool) #Output: True

f.dash()

f.section("Factorial()")

f.subsection("Computing the Factorial of a Single Integer")

n = 5
factorial_n = m.factorial(n)
print(factorial_n) #Output: 120

f.short_dash()

f.subsection("Computing factorials for a range of integers using a for loop")

n = 100
for i in range(n):
    factorial_i = m.factorial(i)
    print(f"The factorial of {i} is {factorial_i}")

f.short_dash()

f.subsection("Using factorail() Function to compute the number of ways to choos 'k' objects frtom 'n' objects")

def n_choose_k(n, k):
    return m.factorial(n)//(m.factorial(k) * m.factorial(n-k))

n = 10
k = 3
n_choose_k_10_3 = n_choose_k(n, k)
print(f"The number of ways the choose {k} objects from {n} objects is {n_choose_k_10_3}")

f.short_dash()

f.subsection("Using a Loop to Calculate Factorial")

n = 5
result = 1
for i in range(1, n+1):
    result *= i

print(f"The factorial of {n} is {result}")

f.short_dash()

f.subsection("Using a Recursive Function to Calculate Factorial")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")

f.dash()
