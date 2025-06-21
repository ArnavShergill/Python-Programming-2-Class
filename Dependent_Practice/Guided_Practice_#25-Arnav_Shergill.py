import formatting as f

f.title("Guided Practice #25")

f.dash()

f.section("Indexing, Slicing, & Immutability Intro")

one_piece = "Monkey D. Luffy"

first_character = one_piece[0]
print(first_character)

f.short_dash()

fifth_character = one_piece[4]
print(fifth_character) # Output: "e"

f.short_dash()

piece = one_piece[4:]
print(piece) # Output: "ey D. Luffy"

f.short_dash()

new_string = one_piece[0].upper()+one_piece[1:]
print(new_string) # Output: Monkey D. Luffy

f.dash()

f.section("Using slice() method")

# Python program to demonstrate string slicing

# String Slicing
string = "ASTRING"

#Using slice constructor
s1 = slice(3) # display everything before index 3
s2 = slice (1,5, 2) # Start at index 1, go to index 5, count every 2
s3 = slice(-1, -12, -2) # start at index -1, go to index -12, count every -2

print(string[s1])
print(string[s2])
print(string[s3])

f.dash()

f.section("Using List/Array Slicing Method")

f.subsection("Example 1")

# List/Array Slicing

string = 'COXMILLCHARGERS'

# Using indexing sequence
print(string[:7])

f.short_dash()

f.subsection("Example 2")

# List/Array Slicing

string = 'COXMILLCHARGERS'

# Using indexing sequence
print(string[:7])
print(string[1:5:2])

f.short_dash()

f.subsection("Example 3")

# List/Array Slicing

string = 'COXMILLCHARGERS'

# Using indexing sequence
print(string[:7])
print(string[1:5:2])
print(string[-1:-12:-2])

f.short_dash()

f.subsection("Example 4")

# List/Array Slicing

string = 'COXMILLCHARGERS'

# Using indexing sequence
print(string[:7])
print(string[1:5:2])
print(string[-1:-12:-2])
print(string[::-1])

f.dash()

f.section("Indexing Strings")

f.subsection("Example 1: Accessing individual characters")

username = "RoblxoGamer123"
print(username[0]) #Output: "R"
print(username[6]) #Output: "G"

f.short_dash()

f.subsection("Example 2: Accessing individual characters")

game_name = "Welcome to Bloxburg"
print(game_name.index("o")) #Output: 4

f.short_dash()

f.subsection("Example 3: Negative Indexing")

favorite_game = "Adopt Me!"
print(favorite_game[-1]) #Output: "!"
print(favorite_game[-5]) #Output: "t"

f.short_dash()

f.subsection("Example 4: Modifying a string using indexing")

message = "I love playing Roblox"
message = message[:14] + " Adopt Me!" + message[21:]
print(message) # Output: I love playing Adopt Me!

f.dash()

f.section("Slicing Strings")

f.subsection("Example 1: Extracting a substring")

username = "RobloxGamer123"
print(username[6:11]) # Output: "Gamer"

f.short_dash()

f.subsection("Example 2: Skipping Characters")

game_name = "Welcome to Bloxburg"
print(game_name[::2]) # Output: "Wloet lxug"

f.short_dash()

f.subsection("Example 3: Reversing a String")

favorite_game = "Adopt Me!"
print(favorite_game[::-1]) #Output: "!eM tpodA"

f.dash()

f.section("Immutability with Strings")

my_string = "Hello"
new_string = "J" + my_string[1:]
print(new_string) # Output: "Jello"

f.dash()

f.section("Iterating Through Strings")

my_string = "Hello, world!"
for character in my_string:
    print(character)

f.short_dash()

f.subsection("Concatenating Strings")

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

f.short_dash()

f.section("Multiplying Strings")

my_string = "Hello"
repeated_string = my_string * 3
print(repeated_string)

f.short_dash()

f.section("Comparing Strings")

password = "secret"
user_input = input("Enter your password: ")
if user_input == password:
    print("\nAccess granted!")
else:
    print("\nAccess granted!")

f.dash()

f.section("In & Not In")

f.subsection("The 'in' operator")

my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list!")
else:
    print("3 is not in the list.")

f.short_dash()

f.subsection("The 'not in' Operator")

my_string = "Hello, world!"
if "z" not in my_string:
    print("The letter 'z' is not in the string.")
else:
    print("The letter 'z' is in the string")

f.dash()
