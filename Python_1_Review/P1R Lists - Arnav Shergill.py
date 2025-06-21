def dash():
    print("\n----------------------------------------------------------------------------------------------------------\n")

def section(section_name):
    print(f"-- {section_name} --\n")

print("--- Python 1 Review: Lists ---")

dash()

section("Introduction to Lists")

# default list
fruits_list = ["apple", "banana", "banana", "cherry", "kiwi", "orange", "mango", "grape", "pineapple", "blueberry", "strawberry", "strawberry"]

dash()

section("Using append() to Add Elements")

fruits_list.append("pear")
# printed in this format for a cleaner and better looking (in my opinion) output
for n in fruits_list:
    print(n)

dash()

section("Using insert() to Add Elements at a Specfiic Position")

#just did as instructions specified
fruits_list.insert(1, "kiwi")

for n in fruits_list:
    print(n)

dash()

section("Using remove() to Delete an Element")

#removed as instructed
fruits_list.remove("kiwi")

for n in fruits_list:
    print(n)

dash()

section("Using pop() to Remove an Element by Index")

popped = fruits_list.pop(1)
print(fruits_list, "\n")
print(popped)

dash()

section("Slicing Lists")

#I put the popped fruits into variables and the variables into a list because I didn't know how to put the popped elements directly into the list
fruit1 = fruits_list.pop(1)
fruit2 = fruits_list.pop(2)
sliced_list = [fruit1, fruit2]
for n in fruits_list:
    print(n)

dash()

section("Modifying Elements")

# I would rather use -1 as index because it is easier than counting all of the elements
fruits_list = ["apple", "banana", "cherry", "kiwi", "orange", "mango", "grape","pineapple", "blueberry", "strawberry", "strawberry"]
fruits_list[-1] = "raspberry"
for n in fruits_list:
    print(n)

dash()

section("Using while Loops with Lists")

#had to use both types of loops to make it work, but it meets the requirements of the instructions. I used a while loop.
while "kiwi" in fruits_list:
    for fruit in fruits_list:
        if fruit == "kiwi":
            fruits_list.remove(fruit)
        else:
            continue

for fruit in fruits_list:
    print(fruit)

dash()

section("Using for Loops with Lists")

#done as specified in instructions
for fruit in fruits_list:
    print(fruit)

dash()

section("Using if Statements with Lists")

#had to put break if true_or_false is true so that the code can stop when it found apple in the list
for n in fruits_list:
    if n == "apple":
        true_or_false = True
        print(true_or_false)
        break
    else:
        true_or_false = False
        print(true_or_false)

dash()

section("Using sort() to Sort Lists")

#used the for loop to print so that it doesn't print the commas and square brackets
fruits_list = ["apple", "banana", "cherry", "kiwi", "orange", "mango", "grape","pineapple", "blueberry", "strawberry"]
fruits_list.sort()
for n in fruits_list:
    print(n)

dash()

section("Using sorted() to View a Sorted List")

#used sorted instead of sort
sorted_fruits_list = sorted(fruits_list)
for n in sorted_fruits_list:
    print(n)

dash()

section("Using extend() to Add Multiple Items")

# I used fruits_list ins tead of extended_list and it didn't work, so I redid the code to where it primarily uses extended_list, and then it worked.
fruits_list = ["apple", "banana", "cherry", "kiwi", "orange", "mango", "grape","pineapple", "blueberry", "strawberry"]
extended_list=["raspberry", "cucumber", "pumpkin"]
extended_list.extend(fruits_list)
extended_list.sort()
for n in extended_list:
    print(n)

dash()
