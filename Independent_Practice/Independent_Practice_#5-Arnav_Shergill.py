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

    # will only run if called upon 
    def describe_restaurant(self):
        """prints out the cousine and opening times for the restaurant"""
        print(f"\nThe {self.restaurant_name} hours are from 12 pm to 9 pm.")
        print(f"The {self.restaurant_name} offers lunch and dinner cuisine for: {self.cuisine_type}")

    # will only run if called upon
    def open_restaurant(self):
        """tells the user that the restaurant is open."""
        print("The restaurant is open now!")

# basic object to show that the class works
my_restaurant = Restaurant("My Restaurant", "American")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

f.dash()

f.section("Three Restaurants")

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

#method example
me.greet_user()

f.dash()
