import formatting as f

f.title("Guided Practice #7")

f.short_dash()

f.section("Parent/Child")

class ParentClass:
    def __init__(self,x):
        self.x = x

class ChildClass(ParentClass):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

f.subsection("Example of Super() Function")

class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        super().greet()
        print("Hi, I'm a student!")

s = Student()
s.greet()

f.dash()

f.section("Inheritance Explanation")

f.subsection("Inheriting Attributes and Methods")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}.")

class Dog(Animal):
    pass

dog = Dog("Fido", "Woof")
dog.speak() # Output: "Fido says Woof."

f.short_dash()

f.subsection("Overriding Methods")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

dog = Dog("Fido", "Woof")
dog.speak() #Output: "Fido barks."

f.short_dash()

f.subsection("Adding New Methods and Attributes")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks loudly.")

dog = Dog("Fido", "Woof")
dog.speak() #Output: "Fido says Woof."
dog.bark()

f.dash()

f.section("Inheritance")

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odomter!")

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the prarent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('Tesla', 'Model S', 2023)
print(my_tesla.get_descriptive_name())

f.dash()

f.section("Defining Attributes & Methods")

class ElectricCar(Car):
    """Respresent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class. Then initialize attribute specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar("Tesla", "Model S", 2023)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

f.dash()

f.section("Overriding Methods")

f.subsection("Instances as Attributes")

class Battery:
    """A simple attempt to mdoel a battery for an electric car."""
    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range == 315

        print(f"This car can go about {battery_range} miles on a full charge.")

class ElectricCar(Car):
    """Respresent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class. Then initialize attribute specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar("Tesla", "Model S", 2023)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

f.dash()
