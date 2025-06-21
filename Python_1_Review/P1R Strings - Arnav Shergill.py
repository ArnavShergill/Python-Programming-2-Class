def dash():
    print("\n---------------------------------------------------------------------------------------\n")

print("---- Python 1 Review: Strings ----")

dash()

print("--- String Slicing ---\n")

print("-- Exercise 1.1 --\n")

s = "PythonIsFun"
#had to end at :6 because if  I ended at :5, it would cut off the last character of the word
print(s[0:6])

print("\n-- Exercise 1.2 --\n")

#there is no end digit becuase the program needs to print the last three digits.
print(s[8:])

dash()

print("--- String Slicing ---\n")

print("-- Exercise 2.1 --\n")

#did sub_list to lst[1:4] since the first digit cannot be included and I need to end it at 4 since if it was at 3, it would cut of the digit 3
lst = [0, 1, 2, 3, 4, 5]
sub_list = lst[1:4]
print(sub_list)

print("\n-- Exercise 2.2 --\n")

#did -2 instead of the positive integer because it is easier and negative splicing does not start at 0. Also only need the last two characters in the list
last_two = lst[-2:]
print(last_two)

dash()

print("--- Using len() ---\n")

print("-- Exercise 3.1 --\n")

#simple, but works
print(len(s))

print("\n--Exercise 3.2 --\n")

#simple, but works
print(len(lst))

dash()

print("--- Using count ---\n")

#put in the variable and then printed it because it just made sense
count_n = s.count("n")
print(count_n)

dash()

print("--- Using find() ---\n")

print("-- Exercise 5.1 --\n")

#named variable find_o because the instructions said to find o, and it seemed like a good name for a variable.
find_o = s.find("o")
print(find_o)

print("\n-- Exercise 5.2 --\n")

#value put in variable to be able to use in if else statement
find_z = s.find("z")

if find_z == -1:
    print(True)
else:
    print(find_z)

dash()

print("--- String Formatters ---\n")

print("-- Exercise 6.1 --\n")

#used this format because I forgot how to do it all the other ways
word = "Python"
number = "3"
love_programming = "I love programming in {} {}"
print(love_programming.format(word, number))

print("\n-- Exercise 6.2 --\n")

#used normal f-string because instruction said to
love_programming = f"I love programming in {word} {number}"
print(love_programming)

dash()
