import formatting as f

f.title("Independent Practice #5")

f.dash()

f.section("Restuarant")

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

# basic object to show that the class works
my_restaurant = Restaurant("My Restaurant", "American")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(0)
my_restaurant.set_number_served(100)

f.dash()

f.section("Three Restaurants")

restaurant = Restaurant("Restaurant", "French")
restaurant.set_number_served(0)
restaurant.set_number_served(100)
restaurant.set_number_served(10000000000)
restaurant.increment_number_served(100)

#same as the example above
my_restaurant = Restaurant("My Restaurant", "American")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#new objects for the concept that a person can make several objects from one class
your_restaurant = Restaurant("Your Restaurant", "Indian")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

their_restaurant = Restaurant("Their Restaurant","Mexican")
their_restaurant.describe_restaurant()
their_restaurant.open_restaurant()

f.dash()

f.section("Users")

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

#example to show class works
me = Users("Arnav", "Shergill", 17, 1, "August 24, 2007", "Photography")

#method examples
me.greet_user()
me.increment_login_attempts()
me.reset_login_attempts()

f.dash()
