import formatting as f

f.title("Guided Practice #19")

f.dash()

f.section("Raising and Catching Errors")

f.subsection("IndexError")

try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception:
    print("Got an error")

print("continuing")

f.short_dash()

f.subsection("IndexError 2.0")

try:
    items = ['a', 'b']
    thrid = items[2]
    print("This won't print")
except IndexError:
    print("Error 1")

print("continuing")

f.short_dash()

f.subsection("ZeroDivisionError")

try:
    x = 5
    y = x/0
    print("This won't print, either")
except IndexError:
    print("error 2")
except ZeroDivisionError:
    print("Error 3")

print("continuing again")

f.dash()

f.section("Handling the ZeroDivisionError Exception")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

f.dash()

f.section("Using Exceptions to Prevent Crashes")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    firstNumber = input("\nFirst Number: ")
    if firstNumber == 'q':
        break
    secondNumber = input("\nSecond Number: ")
    if secondNumber == 'q':
        break
    answer = int(firstNumber) / int(secondNumber)
    print("\n", answer)
    break

f.dash()

f.section("The Else Block")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    firstNumber = input("\nFirst Number: ")
    if firstNumber == 'q':
        break
    secondNumber = input("\nSecond Number: ")
    if secondNumber == 'q':
        break
    try:
        answer = int(firstNumber) / int(secondNumber)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print("\n", answer)
    
    break
    
f.dash()