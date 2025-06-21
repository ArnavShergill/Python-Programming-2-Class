import formatting as f

f.title("Guided Practice #22")

f.dash()

f.section("Assert Exception")

def divide(a, b):
    assert b !=0, "Division by zero"
    return a/b

try:
    result = divide(10, 1)
    print(result)
except AssertionError:
    pass

f.dash()

f.section("Assert Statements")

f.subsection("Loops")

numbers = [1,2,3,4,5]

for num in numbers:
    assert num > 0, "Invalid number"
    print(num)

f.short_dash()

f.subsection("Functions")

def calculate_total(price, quantity):
    assert price >= 0 and quantity >= 0, "Invalid input"
    return price * quantity

try:
    total = calculate_total(-10, 5)
    print(total)
except AssertionError:
    pass

f.short_dash()

f.subsection("Tuples")

person = ("John", "Doe", 30)
assert len(person) == 3, "Invalvid tuple"

f.short_dash()

f.subsection("Lists")

try:
    items = ["apple", "banana", "orange"]
    assert "pear" in items, "Item not found"
except AssertionError:
    pass

f.short_dash()

f.subsection("Dictionaries")

try:
    person = {"name":"John", "age":30}
    assert "email" in items, "Email not found"
except AssertionError:
    pass

f.dash()

f.section("More Assert Statements")

f.subsection("Classes")

class Rectangle:
    def __init__(self, width, height):
        assert width > 0 and height > 0, "Invalid input"
        self.width = width
        self.height = height

    def area(self):
        return self.width * self. height

try:
    rect = Rectangle(-10, 5)
    print(rect.area())
except AssertionError:
    rect = Rectangle(10, 5)
    print(rect.area())

f.dash()
