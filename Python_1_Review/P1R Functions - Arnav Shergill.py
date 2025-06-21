def dash():
    print("\n------------------------------------------------------------------------------------------\n")

print("---- Python 1 Review: User Functions ----")

dash()

print("--- Basic Function Creation and Call ---\n")

print("-- Task 1 --\n")

#def is for defining that the code block is a function and the "display_mesage" is the function name.
# print is the code block
def display_message():
    print("Hello from inside the function!")

print("-- Task 2 --\n")

#display_message is the function name and typed it in proper syntax
display_message()

dash()

print("--- Parameters and Arguments ---\n")

print("-- Task 1 --\n")

#name is the parameter that is passed through and is used in the f-string for formatting. I used f-strings because it is easier for me in my opinion to format it that way
def greet_user(name):
    print(f"Hello, {name}")

print("-- Task 2 --\n")

#my name is used as an argument as specified in the instructions.
greet_user("Arnav")

dash()

print("--- Returning Values ---\n")

print("-- Task 1 --\n")

#I didn't make a third variable for the sum of the two numbers as I could just return the equation itself
def add_numbers(num1, num2):
    return num1 + num2

print("-- Task 2 --\n")

#Here I stored the returned value into a variable and then print it as it was stated in the instructions
result = add_numbers(12, 24)
print(result)

dash()

print("--- Positional Arguments ---\n")

print("-- Task 1 --\n")

#used a f-string again because of it being easy to format. Also used .title() for grammatical reasons
def describe_pet(animal_type, pet_name):
    print(f"You have a {animal_type.title()} named {pet_name.title()}.")

print("-- Task 2 --\n")

#excecuted function
describe_pet("dog", "Whiskers")

dash()

print("--- Keyword Arguments ---\n")

print("-- Task 1 --\n")

#pet_name as whiskers and pet_type as cat
describe_pet(pet_name = "whiskers", animal_type = "cat")

dash()

print("--- Mixing Positional and Keyword Arguments ---\n")

print("-- Task 1 --\n")

#pet_name as tweety and pet_type as bird
describe_pet(animal_type = "bird", pet_name = "tweety")

dash()
