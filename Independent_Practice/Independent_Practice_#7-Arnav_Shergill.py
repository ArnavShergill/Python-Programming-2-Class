import formatting as f

f.title("Independent Practice #7")

f.dash()

f.section("Task 1")

class Restaurant:

    # "__init__" is the initial method that sets each object apart since each "__init__" will be different for each object
    def __init__(self, restaurant_name, cuisine_type):
        """defines the attributes in in the method for the class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def set_number_served(self, default_numbers_served = 0):
        print(default_numbers_served)

    # will only run if called upon 
    def describe_restaurant(self):
        """prints out the cousine and opening times for the restaurant"""
        print(f"\nThe {self.restaurant_name} hours are from 12 pm to 9 pm.")
        print(f"The {self.restaurant_name} offers lunch and dinner cuisine for: {self.cuisine_type}")

    # will only run if called upon
    def open_restaurant(self):
        """tells the user that the restaurant is open."""
        print("The restaurant is open now!")

    number_served = 0

    # Had to do self.number_served for set_number_served and increment_number_served so that it can refer to the same instance
    def set_number_served(self, served):
        self.number_served = served
        print(f"number of customers served:\n{self.number_served}")

    def increment_number_served(self, increment):
        self.number_served = increment + self.number_served
        print(f"number of customers served:\n{self.number_served}")

# Somehow made line 43 redundant. Could have just written it as a function, but it's an independent practice about inheretance, so wrote it as a class, I guess.
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

flavor_list = ["Mint", "Vanilla", "Chocolate", "Strawberry"]
ice_cream_truck = IceCreamStand("Ice Cream Truck", "Ice Cream", flavor_list)
ice_cream_truck.describe_restaurant()
ice_cream_truck.display_flavors()

#ice_cream_stand = IceCreamStand(flavor_list)
#ice_cream_stand.flavors()

f.dash()

f.section("Task 2")

class Users:
    # "__init__" method for the info for the class that sets each object apart
    def __init__(self, first_name, last_name, age, sibling_count, birthday, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sibling_count = sibling_count
        self.birthday = birthday
        self.hobby = hobby

    login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"\nAttmpts to login:\n{self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("\nThe login attempt count has reset to 0")

    # custom greeting for the user but isn't looped since couldn't figure out how to get the attributes from "__init__" and turn into loopable list
    def greet_user(self):
        print(f"The first name is:\n{self.first_name}\n")
        print(f"The last name is:\n{self.last_name}\n")
        print(f"The age is:\n{self.age}\n")
        print(f"The number of siblings are:\n{self.sibling_count}\n")
        print(f"The birthday is:\n{self.birthday}\n")
        print(f"The hobby is:\n{self.hobby}")

class Admin(Users):
    def show_privileges(self):
        privilege_dict = {"add post":True, "delete post":True, "ban user":True}
        for key in privilege_dict:
            print(f"{key.title()}: {privilege_dict[key]}")

admin1 = Admin("Arnav", "Shergill", 17, 1, "August 24, 2007", "Photography")
admin1.show_privileges()

f.dash()

f.section("Task 3")

class Users:
    # "__init__" method for the info for the class that sets each object apart
    def __init__(self, first_name, last_name, age, sibling_count, birthday, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sibling_count = sibling_count
        self.birthday = birthday
        self.hobby = hobby

    login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"\nAttmpts to login:\n{self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("\nThe login attempt count has reset to 0")

    # custom greeting for the user but isn't looped since couldn't figure out how to get the attributes from "__init__" and turn into loopable list
    def greet_user(self):
        print(f"The first name is:\n{self.first_name}\n")
        print(f"The last name is:\n{self.last_name}\n")
        print(f"The age is:\n{self.age}\n")
        print(f"The number of siblings are:\n{self.sibling_count}\n")
        print(f"The birthday is:\n{self.birthday}\n")
        print(f"The hobby is:\n{self.hobby}")

class Privilege:
    def __init__(self, add_post, delete_post, ban_user):
        self.add_post = add_post
        self.delete_post = delete_post
        self.ban_user = ban_user

    def show_privileges( true_false1, true_false2, true_false3):
        privilege_dict = {"add post":true_false1, "delete post":true_false2, "ban user":true_false3}
        for key in privilege_dict:
            print(f"{key.title()}: {privilege_dict[key]}")

class Admin(Users):
    def __init__(self):
        admin_priv = Privilege.show_privileges(True, True, True)

admin1 = Admin()


f.dash()

f.section("Task 4")

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
        battery_range = 0 # Default value
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315
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
    
    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery.battery_size == 75:
            self.battery.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("This car already has the best battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print()
my_tesla.upgrade_battery()
my_tesla.battery.get_range()

f.dash()
