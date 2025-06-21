import formatting as f

f.title("Independent Practice #27")

f.dash()

f.section("Sets")

#Creating a set using curly braces with elements:
my_set = {1, 2, 3}

# Creating an empty set (note: {} creates an empty dictionary)
empty_set = set()

# Creating a set from an iterable (e.g., list) which also removes duplicates:
set_from_list = set([1, 2, 2, 3])

f.short_dash()

f.subsection("Defining a Set and Demonstrating Uniqueness")

numbers = {1, 2, 2, 3, 3, 3, 4, 5}
print("Unique numbers: ", numbers) #Output might be: {1, 2, 3, 4, 5)

f.short_dash()

f.subsection("Membership Testing with Sets")

fruits = {"apple", "banana", "cherry"}
if "banana" in fruits:
    print("Banana is available!")
else:
    print("Banana is not available!")

f.short_dash()

f.subsection("Adding & Removing Elements From a Set")

set1 = set(["Barbosa", "Simba", "Cassandra", "Deepthi", "Cassandra", "Deepthi"])
print(set1)

set1.remove("Cassandra") # Raises a KeyError if the element is not found
print(set1)
# or
set1.discard("Cassandra") # Removes the element if found; does nothing otherwise
print(set1)

f.short_dash()

f.subsection("Using .add()")

set1.add("Sinchana")
print(set1)

f.dash()

f.section("Set Operations")

f.subsection("Unions")

set_a = {1, 2, 3}
set_b = {3, 4, 5}

#Using the .union() method:
combined_set = set_a.union(set_b)
print("Union using .union():", combined_set) # Output: {1, 2, 3, 4, 5}

# Using the | Operator:
combined_set_operator = set_a | set_b
print("Union using | Operator:", combined_set_operator) # Output: {1, 2, 3, 4, 5}

f.short_dash()

f.subsection("Intersections")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Using the .intersection() method:
common_elements = set_a.intersection(set_b)
print("Intersection using .intersection():", common_elements) # Output: {3, 4}

# Using the & operator:
common_elements_operator = set_a & set_b
print("Intersection using & operator:", common_elements_operator) #Output: {3, 4}

f.dash()
