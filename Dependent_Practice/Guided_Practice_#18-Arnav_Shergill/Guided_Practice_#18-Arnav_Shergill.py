import formatting as f

f.title("Guided Practice #18")

f.dash()

f.section("Writing to an Empty File")

filename = "programming.txt"

with open(filename, 'w') as file_object:
          file_object.write("I love programming.")

f.dash()

f.section("Writing Multiple Lines")

f.subsection("Example: Writing without Newlines (Incorrect Output)")

with open("example.txt", 'w') as file:
    file.write("First Line")
    file.write("Second Line")
    file.write("Third Line")

f.short_dash()

f.subsection("Fixing the Issue: Adding Newline for Proper Line Breaks")

with open("example.txt", 'w') as file:
    file.write("First Line\n")
    file.write("Second Line\n")
    file.write("Third Line\n")

f.short_dash()

f.subsection("Writing Multiple Lines at Once Using writelines()")

with open("example.txt",'w') as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)

f.dash()

f.section("Appe nding to a File")

with open("example.txt", "a") as file:
    file.write("This is an added line")

f.dash()
