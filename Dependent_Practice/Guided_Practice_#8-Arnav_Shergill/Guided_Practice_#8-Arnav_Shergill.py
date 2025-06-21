import formatting as f

f.title("Guided Practice #8")

f.dash()

f.section("Importing a Single Class")

from car import Car

my_new_car = Car("audi", "a4", 2023)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

f.dash()

f.section("Storing Multiple Classes in a Module")

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2023)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

f.dash()

f.section("Importing Muultiple Classes from a Module")

from car import Car, ElectricCar

my_beetle = Car("volkswagon", "beetle", 2022)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2021)
print(my_tesla.get_descriptive_name())

f.short_dash()

f.subsection("Importing an Entire Module")

import car

my_beetle = car.Car("volkswagon", "beetle", 2022)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2021)
print(my_tesla.get_descriptive_name())

f.dash()

f.section("Importing All Classes from a Module")

from car import *

f.dash()

f.section("Importing a Module into a Module")

from car import Car
from electric_car import ElectricCar

my_beetle = Car("volkswagon", "beetle", 2022)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2021)
print(my_tesla.get_descriptive_name())

f.dash()

f.section("Using Aliases")

from car import Car
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2021)

f.dash()
