import formatting as f
import math as m

f.clear_console()

f.title("Mini Files Project")

f.dash()

f.section("Task 1: Negative Number Square Root Calculator")

class NegativeNumberError(Exception):
    pass

def calc_sqrt(number):
    try:
        if number < 0:
            raise NegativeNumberError
        elif not isinstance(number, (int, float)):
            raise ValueError
        else:
            result = m.sqrt(number)
    except NegativeNumberError:
        print("The number inputted cannot be a negative number.")
    except ValueError:
        print("The number has to either be an integer or a float.")
    else:
        print(round(result, 2))

f.short_dash()

f.subsection("Attempt 1")

calc_sqrt(3)

f.short_dash()

f.subsection("Attempt 2")

calc_sqrt(-100)

f.dash()

f.section("File Format Validator")

class FileFormatError(Exception):
    pass

with open("data.txt", 'w') as file:
    file.write("DATA")

try:
    with open("data.txt", "r") as file:
        lines = file.read()
    assert lines == "DATA"
except AssertionError:
    print("File is empty!")
else:
    print("The file is in the correct format")
finally:
    f.dash()
    f.section("Bank Account Simulator With Transaction Logging")

class InsufficientFundsError(Exception):
    pass

# I didn't know what format the .log was, so did .csv instead
with open("transactions.csv", 'w') as file:
    file.write("Total, Withdraw, Deposit\n")

class BankAccount:
    def __init__(self, initial_amount):
        self.amount = initial_amount
        with open("transactions.csv", 'a') as file:
            file.write(f"{self.amount}, 0, 0\n")
    
    def withdraw(self, amount):
        try:
            if self.amount < amount:
                raise InsufficientFundsError
            else:
                self.amount = self.amount - amount
        except InsufficientFundsError:
            print("You don't have enough money to withdraw this amount.")
        else:
            print(f"You have successfully withdrew ${amount}.")
            print(f"You have ${self.amount} left")
            with open("transactions.csv", 'a') as file:
                file.write(f"{self.amount}, {amount}, 0\n")
        finally:
            print()
            print("Proccess Complete\n")

    def deposit(self, amount):
        self.amount = amount + self.amount
        print("Deposit complete")
        with open("transactions.csv", 'a') as file:
            file.write(f"{self.amount}, 0, {amount}\n")

myaccount = BankAccount(1000)
myaccount.withdraw(100)
myaccount.withdraw(1000)
myaccount.deposit(500)
myaccount.deposit(100)

f.dash()
