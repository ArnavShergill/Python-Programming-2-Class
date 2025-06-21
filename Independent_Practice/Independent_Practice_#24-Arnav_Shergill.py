import formatting as f

f.clear_console()

f.title("Independent Practice #24")

f.dash()

#checks if variable meets condition and returns true or false.
f.section("Task 1: .isxxxx()")

string = "May the force be with you"

print(string.isalnum())

f.short_dash()

string = "Live long and prosper"
print(string.isalpha())

f.short_dash()

string = "I'll be back"
print(string.isdigit())

f.short_dash()

string = "to infinity and beyond!"
print(string.islower())

f.short_dash()

string = "Winter is coming"
print(string.isspace())

f.short_dash()

string = "Just Do It"
print(string.istitle())

f.short_dash()

string = "Houston, we have a problem"
print(string.isupper())

f.dash()

# converts singular characters and numbers to ASCII and back
f.section("Task 2: ord() & chr()")

def ascii_value(character):
    char = ord(character)
    print(f"The ASCII value for {character} is {char}.")

def unicode_character(num):
    char = chr(num)
    print(f"The value for {num} is {char}.")

ascii_value('A')

unicode_character(165)

f.dash()

# Converts string from string to ASCII and back
f.section("Task 3: Strings & Lists")

string = "Hello World!"

string_in_ascii = []

def string_to_ascii(string):
    char_list = string.strip()
    for char in char_list:
        num = ord(char)
        print(f"The ASCII value for '{char}' is '{num}'.")
        string_in_ascii.append(num)

def ascii_to_string(list):
    for num in list:
        print(f"The alphanumeric value for '{num}' is '{chr(num)}'.")

string_to_ascii(string)

f.short_dash()

ascii_to_string(string_in_ascii)

f.dash()