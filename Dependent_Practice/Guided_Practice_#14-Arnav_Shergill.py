import formatting as f

f.title("Guided Practice #14")

f.dash()

f.section("hypot()")

import math

a = 3
b = 4
c = math.hypot()

print(c) #Output: 5.0

f.short_dash()

f.subsection("Example with Booleans")

a = 3
b = 4
is_right_triangle = (a**2 + b**2 == math.hypot(a,b)**2)

if is_right_triangle:
    print("This is a right triangle!")
else:
    print("This is not a right triangle")

f.short_dash()

f.subsection("Example with Strings")

player_name = "Steve"
a =3
b = 4
c = math.hypot(a, b)

message = f"Hello {player_name}! The length of the hyptenuse is {c}."

print(message)

f.short_dash()

f.subsection("Example with Numbers & Loops")

for i in range(1, 11):
    a = i
    b = i + 1
    c = math.hypot(a, b)
    print(f"the length of the hypotenuse for sides {a} and {b} is {c}.")

f.short_dash()

f.subsection("Example with Functions (methods)")

def distance(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    return math.hypot(dx, dy)

# Calculate the distance between two points: (0, 0) and (3, 4)
d = distance(0,0,3,4)

print(f"The distance between (0, 0) and (3, 4) is {d}")

f.dash()

f.section("sqrt()")

f.subsection("Using sqrt() in a Function")

def hypotenuse(a,b):
    """Calculate the length of the hypotenuse of a right triangle"""
    c = math.sqrt(a**2+b**2)
    return c

# Find the length of the hypotenuse of a tirnagle with sides 3 and 4

a = 3
b = 4
c = hypotenuse(a, b)
print(f"The hypotenuse of the triangle with sides {a} and {b} is {c:2f}")

f.short_dash()

f.subsection("Using sqrt() in a Class")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius

    def surface_area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4/3) * math.pi * self.radius**3

#Create a circle with radius 5
r = 5
circle = Circle(r)
print(f"The area of the circle with radius {r} is {circle.area():.2f}.")
print(f"The circumference of the cirlce is {circle.circumference():.2f}.")
print(f"The diameter of the circle is {circle.diameter():.2f}")
print(f"The surface area of the sphere with radius {r} is {circle.surface_area():.2f}.")
print(f"The volume of the sphere with radius {r} is {circle.volume():.2f}.")

f.short_dash()

f.section("Using sqrt() in an If Statement")

x = 9

if math.sqrt(x) % 1 == 0:
    print(f"{x} is a perfect square")
else:
    print(f"{x} is not a pefect square")

f.short_dash()

f.subsection("Using sqrt() in a Loop")

for i in range(1,11):
    print(f"The square root of {i} is {math.sqrt(i):.2f}")

f.short_dash()

f.subsection("Using sqrt() in a List Comprehension")

numbers = [1, 4, 9, 16, 25]
square_roots = [math.sqrt(n) for n in numbers]
print(square_roots)

f.dash()
