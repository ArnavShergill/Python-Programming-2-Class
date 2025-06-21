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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)
