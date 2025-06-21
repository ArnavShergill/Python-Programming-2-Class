import formatting as f

f.title("Independent Practice #10")

f.dash()

f.section("Task 1: Math")

def addition(*args):
    """returns the sum of any group of numbers"""
    sum = 0
    for num in args:
        sum += num
    return sum

print(addition(1,2,3,4,5))

f.short_dash()

def multiplication(*args):
    """returns the product of any group of numbers"""
    product = 1
    for num in args:
        product *= num
    return product

print(multiplication(1,2,3,4,5))

f.short_dash()

def concatenation(*args):
    """Concatinates any amount of strings given in parameter of function"""
    concatenated = ""
    for string in args:
        concatenated += string + " "
    return concatenated

print(concatenation("The", "QWERTY", "keyboard", "layout", "is", "the", "default", "keyboard", "layout."))

f.short_dash()

def print_kwargs(first_name, middle_name, last_name):
    """Uses kwargs to print a user friendly output"""
    print("first name:", first_name.title())
    print("middle name:", middle_name.title())
    print("last name:",  last_name.title())

kwargs = {"first_name":"billy", "middle_name":"bob", "last_name":"joe"}

print_kwargs(**kwargs)

f.dash()

f.section("Task 2: Animal Class")

class Animal:
    def __init__(self, **kwargs):
        """Uses **kwargs to get the attributes needed for the class instance"""
        self.name = kwargs.get("name")
        self.species = kwargs.get("species")

    def speak(self):
        """returns the instance name and instance species in a user friendly output"""
        return "I am {} the {}".format(self.name, self.species)

class Dog(Animal):
    def __init__(self, **kwargs):
        """gets the name and species of the instance from the parent class using the super() function"""
        super().__init__(**kwargs)
        self.breed = kwargs.get("breed")
        self.color = kwargs.get("color")

    def bark(self):
        """returns the output of what a dog would say"""
        return "Woof!"

class Cat(Animal):
    def __init__(self, **kwargs):
        """gets some attributes from parent class using super() function and the rest from the kwargs.get() function"""
        super().__init__(**kwargs)
        self.breed = kwargs.get("breed")
        self.color = kwargs.get("color")

    def meow(self):
        """returns output for what a cat would say"""
        return "Meow!"

my_dog = Dog(name = "Clifford", species = "Dog", breed = "Unknown", color = "Red")

my_cat = Cat(name = "Garfield", species = "Cat", breed = "Unknown", color ="Orange")

print(my_dog.speak())
print(my_dog.bark())
print(my_cat.speak())
print(my_cat.meow())

f.short_dash()

def animal_speak(Animals):
    """Takes an Animal instance and calls its speak method"""
    return Animals.speak()

animal_list = [my_dog, my_cat]

for animal in animal_list:
    print(animal_speak(animal))

f.dash()