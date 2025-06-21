import formatting as f

f.clear_console()

f.title("Object Oriented Programming")

f.dash()

f.section("Object Oriented Programming")

f.subsection("What is a Class")

print("- OOP in Simple Terms -\n")

#This is like our cookie cutter
class Superhero:
    health = 100
    speed = 10

f.short_dash()

f.subsection("What is an Object?")

#Making an oibject from our Superhero class
ironman = Superhero()
print(ironman.health) #Output: 100

f.short_dash()

f.subsection("Extending Classes")

"""
Why use classes?

1) Reuse Code: Make many objects from one class.
2) Organize Code: Keep related information and actions together.
3) Easy to Change: Update the class once, and all objects get the update
"""

#Extending the Superhero class
class SuperheroWithSpaceMove(Superhero):
    special_move = "Laser Beam"

f.dash()

f.section("Classes & Obects Glossary")

word_definition = {"Attribute":"One of the named data items that makes up an instance.",
                   "Class":"A class can be thought of as a template for the objects that are instances of it. It defines a data type. A class can be provided by the Python system or be user-defined.",
                   "Initializer Method":"A special method in Python (called __init__) that is invoked automatically to set a newly-created object’s attributes to their initial (factory-default) state.",
                    "Instance":"An object whose type is of some class. Instance and object are used interchangeably.",
                    "Method":"A function that is defined inside a class definition and is invoked on instances of that class.",
                    "Object":"A compound form of data that is often used to model a thing or concept in the real world. It bundles together the data and the operations that are relevant for that thing or concept. It has the type of its defining class. Instance and object are used interchangeably.",
                    "Object-Oriented Programming":"A powerful style of programming in which data and the operations that manipulate it are organized into classes and methods.",
                    "Object-Oriented Language":"A language that provides features, such as user-defined classes and inheritance, that facilitate object-oriented programming."}

for key in word_definition:
    print(f"{key}: {word_definition[key]}")

f.dash()

f.section("Magic Methods")

Magic_Methods = {"__init__":"Constructor for the class, called when a new object is created.",
                 "__del__":"Destructor, called when an object is deleted.",
                 "__str__":"Defines behavior for when str() is called on an instance of your class.",
                 "__repr__":"Defines behavior for when repr() is called, or when you use backticks in Python 2.x.",
                 "__add__, __sub__, __mul__, __truediv__":"Define behavior for operators +, -, *, / respectively.",
                 "__getitem__, __setitem__, __delitem__":"Allow you to use square bracket notation to access, set, and delete elements.",
                 "__eq__, __ne__, __lt__, __le__, __gt__, __ge__":"Define behavior for comparison operators like ==, !=, <, <=, >, >=."}

for word in Magic_Methods:
    print(f"{word}: {Magic_Methods[word]}")

f.dash()

f.section("Class Properties")

f.subsection("Class Special Properties")

class Dog:
    pass

print(Dog.__name__) #Output "Dog"

print("\n__name__: This property returns the name of the class as a string. For example, if you define a class called MyClass, the __name__ property of the class object will be the string 'MyClass'. The __name__ property is commonly used in conjunction with other built-in functions such as isinstance() and type().")

# If this code is in a file named animals.py
class Dog:
    pass

print(Dog.__module__)

print("__module__: This property returns the name of the module in which the class is defined. For example, if you define a class called MyClass in a module called my_module, the __module__ property of the class object will be the string 'my_module'. The __module__ property is useful for debugging and introspection, and can be used to check whether a particular class is defined in the same module as the calling code.")

class dog:
    pass

class Puppy:
    pass

print(Puppy.__bases__) #Output: (<class '__main__.Dog'>,)

print('__bases__: This property returns a tuple of base classes from which the class inherits. For example, if you define a class called MySubclass that inherits from MyClass, the __bases__ property of the MySubclass class object will be a tuple containing the MyClass class object. If MyClass itself inherits from other classes, those classes will also appear in the __bases__ tuple. The __bases__ property is used extensively in object-oriented programming to implement inheritance and polymorphism.')

f.dash()

f.section("Creating & Using a Class")

f.subsection("Creating the Dog Class")

class Dog:
    """A simple attempt to model a Dog."""

    def __init__(self, name, age):
        """Initalize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a Dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
            """Simulate rolling over in response to a command."""
            print(f"{self.name} rolled over!")

f.dash()

f.section("Making an Instance From a Class")

my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

f.short_dash()

f.subsection("Calling Methods")

my_dog.sit()
my_dog.roll_over()

f.dash()

f.section("Creating Multiple Instances")

my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"My_dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print()

print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()

f.dash()

