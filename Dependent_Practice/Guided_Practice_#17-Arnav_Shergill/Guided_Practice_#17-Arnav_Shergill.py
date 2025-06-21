import formatting as f

f.clear_console()

f.title("Guided Practice #17")

f.dash()

f.section("Reading a File")

filename = open("ccdata.txt")

with open ("ccdata.txt", 'r') as file_object:
    lines = file_object.read()

print(lines)
filename.close()

f.dash()

f.section("Iterating over lines in a file")

filename = open("ccdata.txt", 'r')

for aline in filename:
    values = aline.split()
    print("In", values[0], "the average temperature was", values[1], "C and CO2 emmisions were", values[2], "gigatons")

filename.close()

f.dash()

f.section("Reading From a File")

with open("pi_digits.txt") as file_object:
    contents = file_object.read()

print(contents)
print(contents.rstrip())

f.dash()

f.section("Reading Line by Line")

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

f.dash()

f.section("Making a list of Lines from a File")

filename = 'pi_digits.txt'

with open(filename)as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

f.short_dash()

f.subsection("Working with a File's Contents")

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

f.dash()

f.section("Large Files: One Million Digits")

filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string+= line.rstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

f.short_dash()

f.subsection("Birthday")

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("\nYour birthday appears in the first million digits of pi!")
else:
    print("\nYour birthday does not appear in the first million digits of pi")

f.dash()
