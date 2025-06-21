import formatting as f

f.title("Introduction to the Join Method")

f.dash()

names = ["Alice", "Bob", "Charlie"]
result = ", ".join(names)
print(result) #Output: "Alice, Bob, Charlie"

f.dash()

f.section("Join & Dictionaries")

f.subsection("Examples: Joining Dictionary Keys")

my_dict = {"name": "Alice", "job": "Engineer", "city": "New York"}

joined_keys = ", ".join(my_dict.keys())
print(joined_keys) #Output: "name, job, city"

f.short_dash()

f.subsection("Example: Joining Dictionary Values")

joined_values = ", ".join(my_dict.values())

print(joined_values) #Output: "Alice, Engineer, New York"

f.short_dash()

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

joined_values = ", ".join(str(value) for value in my_dict.values())
print(joined_values) #Output: "Alice, 30, New York

f.dash()

f.section("Split & Dictionaries")

f.subsection("Splitting Dictionary Values")

my_dict = {"fruits": "apple, banana, cherry", "vegetables": "carrot, spinach, kale"}

#splitting the "fruits" value on commas
split_fruits = my_dict["fruits"].split(", ")
print(split_fruits) #["apple", "banana", "cherry"]

#Splitting the Vegetables" Value
split_veggies = my_dict["vegetables"].split(", ")

f.short_dash()

f.subsection("Parsing a String to Build a Dictionary")

# Prompt the user for input
data_string = input("enter your key-value pairs in the format: key:value; key:value: .../nExample name:Alice; job:Engineer;city: New York\n\nYour input: ").strip()

#Split the input string on semicolons to separate each "key:value" pair
pairs = data_string.split(";")

#Create an empty dictionary to store the parsed data
parsed_dict = {}

for pair in pairs:
    #for each pair, split on the colon to separate the key from the value
    key, value = pair.split(":")

    #Add the key-value pairto the dictionary
    parsed_dict[key] = value

#print the resulting dictionary
print("\nParsed dictionary:")
print(parsed_dict)

f.dash()
