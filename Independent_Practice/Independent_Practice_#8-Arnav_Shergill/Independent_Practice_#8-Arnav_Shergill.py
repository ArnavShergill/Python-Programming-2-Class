import formatting as f

f.title("Independent Practice #7")

f.dash()

f.section("Task 1 - Imported Restaurant")
#used commas in the import so that I don't have to use 2 imports
from restaurant import Restaurant, IceCreamStand

#did all of the methods to show that my import worked
My_Restaurant = Restaurant("My Restaurant", "American")
My_Restaurant.describe_restaurant()
My_Restaurant.open_restaurant()
My_Restaurant.set_number_served(100)

f.dash()

f.section("Task 2 - Imported Admin")

from user import Users, Admin, Privilege

# adjusted the class and method so that  the method would not be automatically called when instance is made.
admin1 = Admin("Arnav", "Shergill", 17, 1, "August 24, 2007", "photography")
admin1.admin_priv()

f.dash()

f.section("Task 3 - Multiple Modules")

from privileges import Admin, Privilege

# Made the modules work in the way where the main file works with  the same code but with a different instance.
admin2 = Admin("Arnav", "Shergill", 17, 1, "August 24, 2007", "photography")
admin2.admin_priv()

f.dash()
