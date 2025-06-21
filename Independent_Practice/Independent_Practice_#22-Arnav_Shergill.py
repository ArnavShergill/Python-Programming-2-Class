def dash():
    print("\n----------------------------")

def section(section_name):
    print(f"\n--- {section_name} ---\n")

print("\n---- Independent Practice #22 ----")

section("Mario Kart")

def check_kart(top_speed, acceleration, weight):
    """Checks if the values are correct. If incorrect will give error, else will output results"""
    try:
        assert 0 < top_speed <= 200, "Top speed is incorrect"
        assert 0 < acceleration <= 10, "Acceleration is incorrect"
        assert 0 < weight <= 500, "Weight is incorrect"
    except AssertionError:
        print("\nOne of the values is not correct.")
        print("Make sure to double check the values before trying again.")
    else:
        print("\nKart is eligible to race.")

# All correct values
check_kart(200, 10, 1)

# Incorrect top speed
check_kart(201, 10, 1)

#Incorrect acceleration
check_kart(200, 11, 1)

# Incorrect Weight
check_kart(200, 10, 501)

dash()

section("Doctor Mario")

def check_capsule(color, direction):
    """Will check if values are correct and if requirements are met. If met and correct, will output result else will give error"""
    try:
        assert len(color) == 1, "Invalid input for color"
        assert len(direction) == 1, "Invalid input for direction"
    except AssertionError:
        print("Virus cancellation failed due to invalid input.\n")
    else:
        print("Capsule can eliminate virus.")

# Incorrect direction and color
check_capsule("red", "down")

# Incorrect direction
check_capsule("r", "down")

# Incorrect color
check_capsule("red", "d")

# Correct color and direction
check_capsule("r", "d")

dash()

section("Metriod Prime")

def check_energy(current_energy, weapon_energy):
    """Will check if character has enough energy. If not, will error, else will give result"""
    try:
        assert current_energy > 0, "Not enough energy"
        assert weapon_energy > 0, "Not enough weapon energy"
    except AssertionError:
        print("Not enough energy to fire weapon!\n")
    else:
        print("Samus can fire her weapon.")

# Insufficient weapon energy
check_energy(1, 0)

# Insufficient current energy
check_energy(0, 1)

# Insufficient current energy and weapon energy
check_energy(0, 0)

# Sufficient current energy and weapon energy
check_energy(1, 1)

dash()
