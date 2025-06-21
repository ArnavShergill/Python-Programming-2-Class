import formatting as f

f.title("Guided Practice #24")

f.section("Encoding Standards")

# Get the ASCII code point for a character
print(ord("A")) # Output: 65

# Convert an ACSII code point back into a character
print(chr(65))

f.short_dash()

f.subsection("UNICODE")

#Use a Unicode escape sequence to represent a character
print("\u2764") #Output: ❤

# Get the UNICODE code point for a character
print(ord('❤')) # Output: 10084

# Encode a strin gin UTF-8 format
s = '\xF0\x9F\x98\x8D'
utf8_bytes = s.encode("utf-8")
print(utf8_bytes)

#Decode a UTF-8 byte string back into a string
utf8_str = utf8_bytes.decode("UTF-8")
print(utf8_str) #output: ð

f.dash()

f.section("Code Points")

#Get the code point for a character
print(ord('a'))

f.short_dash()

#convert a code point back into a character
print(chr(65))

f.short_dash()

f.subsection("ASCII Code Point")

print(ord('a')) #output: 65

print(ord("❤")) #output: 10084

f.short_dash()

f.subsection("More than 1 Code Point")

print(ord("\U0001F60D")) #Output: 128525

print(chr(65))

print(chr(10084))

print(chr(128525))

f.dash()

f.section("CHR & ORD")

f.subsection("Addition")

num1 = '5'
num2 = '6'
sum = chr(ord(num1) + ord(num2))
print("The sum of", num1, 'and', num2, 'is', sum)

f.short_dash()

f.subsection("Subtraction")

num1 = '6'
num2 = '4'
diff = chr(ord(num1) - ord(num2))
print("The differnece between", num1, 'and', num2, 'is', diff)

f.short_dash()

f.subsection("Multiplication")

num1 = '4'
num2 = '5'
product = chr(ord(num1) * ord(num2))

print(*"The product of", num1, 'and', num2, 'is', product)

f.short_dash()

f.subsection("Division")

num1 = '1'
num2 = '2'
quotient = chr(ord(num1) // ord(num2))
print("The quotient of", num1, 'and', num2, 'is', quotient)

f.dash()

f.section("ASCII Characters")

string = "Have a cutesie day!"
for char in string:
    code = ord(char)
    print(char, "has the ASCII code", code)

codes = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 111, 33]
for coe in codes:
    char = chr(code)
    print("The ASCII code", code, "corresponds to the character", char)

f.dash()

f.section("Built-in String Methods")

f.subsection(".isxxx()")

# Check if a string is all uppercase
string1 = "HELLO WORLD"
print(string1.isupper()) #Output: True

#Check if a string is all numeric
string2 = "123"
print(string2.isnumeric()) #Output: True

f.short_dash()

f.subsection(".join()")

#Join a list of strings witha comma delimiter
my_list = ["apple", "banana", "orange"]
result = ", ".join(my_list)
print(result) # Output: "apple, banana, orange"

f.short_dash()

f.subsection(".split")

# Split a string into a list of words
my_string = "Hello world, how are you?"
result = my_string.split()
print(result)

#Split a string on a comma delimiter
my_string = "apple, banana,orange"
result = my_string.split(",")

print(result) # Output: ['apple', 'banana', 'orange']

f.short_dash()

f.subsection(".sort()")

my_list = ["apple", "banana", "orange"]

my_list.sort()

print(my_list) #Output: ['apple', 'banana', 'orange']

f.short_dash()

f.subsection(".sorted()")

# Sorted a list of strings using the sorted() function
my_list = ["apple", "banana", "orange"]
result = sorted(my_list)

print(result) # Output: ['apple', 'banana', 'orange']

f.short_dash()

f.subsection(".find()")

# Find the index of a substring, or return -1 if it is not found
my_stirng = "Hello world"
result = my_string.find("world")

print(result)

f.short_dash()

f.subsection(".rfind")

my_string = "Hello world, welcome to Python"
index = my_string.rfind("o")
print(index) #Output: 28

f.dash()