import formatting as f

f.title("Guided Practice #6")

f.dash()

f.section("Working with Classes & Instances")

f.subsection("The Car Class")

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2023)
print(my_new_car.get_descriptive_name())

f.dash()

f.section("isinstance() Function")

class MyClass:
    pass

class MySubclass(MyClass):
    pass

obj1 = MyClass()
obj2 = MySubclass()

print(isinstance(obj1, MyClass)) # Output: True
print(isinstance(obj2, MyClass)) # Output: True
print(isinstance(obj1, MySubclass)) # Output: False
print(isinstance(obj2, MySubclass)) # Output: True

f.short_dash()

x = 5
y = 'hello'
z = [1, 2, 3]

print(isinstance(x, int)) # Output: True
print(isinstance(y, str)) # Output: True
print(isinstance(z, (list, str))) # Output: True

f.dash()

f.section("Setting a Default Value")

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

my_new_car = Car('audi', 'a4', 2023)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

f.dash()

f.section("Modifying Attribute Values")

f.subsection("Modifying an Attribute's Value Directly")

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

f.short_dash()

f.subsection("Modifying an Attribute's Value Through a Method")

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

my_new_car = Car('audi', 'a4', 2023)
print(my_new_car.get_descriptive_name())
print()
my_new_car.update_odometer(23)
my_new_car.read_odometer()

f.dash()

f.section("Incrementing an Attributes Value")

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

my_used_car = Car('Subaru', 'Outback', 2022)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

f.dash()

f.section("Introspection")

class MyClass:
    def __init__(self):
        self.public_var = "This is a public variable"
        self.__private_var = "This is a private variable"

obj = MyClass()

print(hasattr(obj, 'public_var')) # Output: True
print(hasattr(obj, '__private_var')) # Output: False

f.dash()

f.section("__dict__ Introduction")

class MyClass:
    class_var = "class value"

    def __init__(self):
        self.instance_var = "instance value"

obj = MyClass()
print(obj.__dict__) #Output: { 'instance_var': 'instance value'}
print(MyClass.__dict__) #Output: {..., 'class_var': 'class value', ...}

f.short_dash()

class MyClass:
    pass

obj = MyClass()
obj.__dict__["new_attr"] = 'new value'
print(obj.__dict__) #Output: {'new_attr': 'new value'}

f.dash()

f.section("__dict__ Property")

class MyClass:
    x=5
    def __init__(self):
        self.y = 10

print(MyClass.__dict__)

f.short_dash()

class MyClass:
    def __init__(self):
        self.x = 5
        self.y = 10

obj = MyClass()
print(obj.__dict__)

f.short_dash()

class MyClass:
    x = 5
    def __init__(self):
        self.y = 10

print(MyClass.__dict__)
obj.__dict__['x'] = 10
print(MyClass.x)

obj = MyClass()
print(obj.__dict__)
obj.__dict__['y'] = 20
print(obj.y)

f.dash()

f.section("Private Components")

class MyClass:
    def __init__(self):
        self.public_var = "This is a public variable"
        self.__private_var = "This is a private variable"

    def get_private_var(self):
        return self.__private_var

obj = MyClass()

print(obj.public_var) #Output: This is a public variable
#print(obj.__private_var) #Raises an Attribute Error

print(obj.get_private_var()) #Output: this is a private variable

f.short_dash()

class MyClass:
    def __init__(self):
        self.public_var = "This is a public variable"

    def __private_method(self):
        ("This is a private method")

    def public_method(self):
        print("This is a public method")
        self.__private_method()

obj = MyClass()

obj.public_method() #Output: This is a public method \n This is a private method
#obj.__private_method() #Raises an Attribute Error

f.dash()
