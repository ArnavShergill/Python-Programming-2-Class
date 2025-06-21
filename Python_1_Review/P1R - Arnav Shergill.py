def dash():
    print("\n--------------------------------------\n")

print("--- Python 1 Input Review ---")

dash()

print("-- Basic Input with 'input()' --\n")

#input and output
Username = input("What is your name? ")
print("Hello, " + Username)

dash()

print("-- Combining Input and Output --\n")
#input two numbers and output result
num1 = input("Input the first number: ")
num2 = input("Input the second number: ")
print("\nThe sum of " + num1 + " and " + num2 + " is " + str(int(num1) + int(num2)) + ".")

dash()

print("-- Advanced Output formatting --\n")
#using f-string to concaninate variables and string
print(f"{Username}, you have chosen the numbers {num1} and {num2} and the total is {str(int(num1) + int(num2))}\n")
num3 = int(num1)+int(num2)
txt = "{name}, you have chosen the numbers {number1} and {number2} and the total is {number3}"
print(txt.format(name = Username, number1 = num1, number2 = num2, number3 = num3))


dash()
