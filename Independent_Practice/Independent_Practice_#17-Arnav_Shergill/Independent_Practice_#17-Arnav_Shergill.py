import formatting as f

f.title("Independent Practice #17")

f.dash()

f.section("Learning Python")

#reads per line
with open("learning_python.txt") as filename:
    lines = filename.read()

print(lines)

f.short_dash()

#loops through file lines

filename = open("learning_python.txt")

for line in filename:
    values = line.split()
    print(" ".join(values))

filename.close()

f.short_dash()

# does in list
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)

f.dash()

f.section("Learning C")

#replaces python with C++
filename = open("learning_python.txt", "r")

#decided to do inefficient and dumb way instead of thinking too much about it, but it works.
for line in filename:
    values = line.split()
    values.pop(1)
    values.insert(1, "C++")
    print(" ".join(values))

f.dash()
