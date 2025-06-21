import formatting as f

f.title("Independent Practice #19")

f.dash()

f.section("Task 1")

# This function divides two numbers entered by the user.
def divide():
    # This loop will continue to prompt the user for input until valid input is entered.
    while True:
        try:
            # The user inputs two numbers.
            num1 = int(input("Input first number: "))
            num2 = int(input("Input second number: "))
            # The result of the division is calculated.
            result = num1 / num2
        # If the user attempts to divide by 0, a ZeroDivisionError is caught.
        except ZeroDivisionError:
            # The user is informed that they cannot divide by 0.
            print("\nYou cannot divide by 0. It is impossible!\n")
            # The loop continues.
            continue
        # If there are no errors, the result is printed and the loop breaks.
        else:
            print("\n", result)
            break

# The divide function is called.
divide()

f.dash()

f.section("Task 2")

# The filename is set to "characters.txt".
filename = "characters.txt"

# The file is opened in write mode.
with open(filename, 'w') as file:
    # The following characters are written to the file.
    file.write("Characters:\n")
    file.write("Steve\n")
    file.write("Alex\n")
    file.write("Creeper\n")
    file.write("Zombie\n")
    file.write("Skeleton\n")
    file.write("Witch\n")
    file.write("Wither Skeleton\n")
    file.write("Blaze\n")
    file.write("Piglin\n")
    file.write("Ender Dragon\n")
    file.write("Wither\n")

# The file is opened in read mode.
with open(filename, 'r') as file:
    # The lines from the file are read into a list called lines.
    try:
        lines = file.readlines()
    # If the file cannot be found, a FileNotFoundError is caught.
    except FileNotFoundError:
        # The user is informed that the file cannot be found.
        print("This file cannot be found!")

    # This loop will continue to prompt the user for input until valid input is entered.
    while True:
        try:
            user_character = int(input("Please input a digit between 1 and 11: "))
            # If the user input is not between 1 and 11, an IndexError is raised.
            if user_character < 1 or user_character > 11:
                raise IndexError
            print("\nYou have chosen:\n", lines[user_character].rstrip())
            break
        # If the user inputs a number outside the range of 1 and 11, an IndexError is caught.
        except IndexError:
            # The user is informed that their input is not within the range of 1 and 11.
            print("\nThat is not within the range of 1 and 11. Try Again!\n")
            # The loop continues.
            continue
        # If the user inputs a value that is not a number, a ValueError is caught.
        except ValueError:
            # The user is informed that their input is not a number.
            print("\nThe inputted value is not a number. Try Again!\n")
            # The loop continues.
            continue
        # If the file is not found, a FileNotFoundError is caught.
        except FileNotFoundError:
            # The user is informed that the file is not found and the program quits.
            print("File is not found.")
            quit

f.dash()
