import formatting as f
import math as m

f.title("Independent Practice #14")

f.dash()

f.section("Task 1 - The Vet")

class Coordinates:
    def __init__(self):
        """gets the coords from user for the current location and the destination location and checks whether or not it is the correct integer/float"""
        while True:
            try:
                self.self_coords = [int(i) for i in input("What are the x and y coordinates of your location?\nPlease separate the values with a comma and space: ").split(", ")]
                self.dest_coords = [int(i) for i in input("\nWhat are the x and y coordinates of your destination?\nPlease separate the values with a comma and space: ").split(", ")]
                break
            except ValueError:
                print("You have to enter an integer or float, nothing else. Try again.")
                continue

    def calculate_distance(self):
        """calculates the distance between the two locations formats for a nice output for the user"""
        xd = self.self_coords[0] - self.dest_coords[0]
        yd = self.self_coords[1] - self.dest_coords[1]
        return f"The distance between you and the vet is {m.hypot(xd, yd):.2f} miles."

vet_visit = Coordinates()
print(vet_visit.calculate_distance())

f.dash()

f.section("Task 2 - Cat Tower")

#gets all three dimensions from user
x = int(input("What is the 1st dimension?\n"))
y = int(input("\nWhat is the 2nd dimension?\n"))
z = int(input("\n What is the 3rd dimension?\n"))

diagonal = m.hypot(z, m.hypot(x, y))

#if diagonal is less than 6, then give warning, else print the diagonal
if diagonal < 6:
    print(f"\nThe diagonal dimension for this tower is {diagonal:.2f} feet, but it might not be big enough for your cats")
else:
    print(f"\nThe diagonal dimension for this tower is {diagonal:.2f} feet.")

f.dash()

f.section("Task 3 - Age Gap")

while True:
    # loops until the user gives the right input type
    try:
        Barbosa = int(input("What is the age of Barbosa?\n"))
        Simba = int(input("\nWhat is the age of Simba?\n"))
        break
    except ValueError:
        print("\nAge has to be a number, nothing else. Try again.")
        continue

Simba = Simba * 12
Barbosa = Barbosa * 12

age_diff = Barbosa - Simba

print(f"\nThe age difference of Barbosa and Simba is {age_diff:.2f} months")

f.dash()
