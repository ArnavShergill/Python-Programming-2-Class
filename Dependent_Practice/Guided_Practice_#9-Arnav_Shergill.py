def dash():
    print("\n-------------------------------------------------------------------------------------------------\n")

def short_dash():
    print("\n--------------------------------------\n")

def section(section_name):
    print(f"--- {section_name} ---\n")

def subsection(subsection_name):
    print(f"-- {subsection_name} --\n")

print("---- Guided Practice #9 ----")

dash()

section("Creating Polymorphic Classes")

class Shark:
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("the shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")

class Clownfish:
    def swim(self):
        print("the clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")

sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()

dash()

section("Polymorphism with Class Methods")

sammy = Shark()
casey = Clownfish()

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()
    print()

dash()

section("Polymorphism with a Function")

subsection("Polymorphing: Wild Force")

def in_the_pacific(fish):
    fish.swim()

sammy = Shark()
casey = Clownfish()

in_the_pacific(sammy)
in_the_pacific(casey)

dash()
