import formatting as f

f.title("Guided Practice #11")

f.dash()

f.section("Encapsulation")

f.subsection("Defining a Class")

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

f.short_dash()

f.subsection("Public Attributes")

account = BankAccount("123456789", 1000)
print(account.balance) # Output: 1000

f.short_dash()

f.subsection("Protected Atributes")

class BankAccount:
    def __init__(self, account_number, balance, interest_rate):
        self._account_number = account_number
        self._balance = balance
        self._interest_rate = interest_rate

    def calculate_interest(self):
        return self._balance *self._interest_rate

f.short_dash()

f.subsection("Private Attributes")

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def __process_transaction(self, amount):
        if amount < 0:
            raise ValueError("Transaction amount must be positive")
        self.__balance += amount

        def deposit(self, amount):
            BankAccount.__process_transaction(amount)

        def withdraw(self, amount):
            if self.balance <amount:
                raise ValueError("Insufficient funds.")
            self.__process_transaction(-amount)

f.dash()

f.section("Name Mangling")

class MyClass:
    def __init__(self):
        self.__private_var = "This is a private variable"

    def __private_method(self):
        print("This is a private method")

obj = MyClass()

#Accessing the private variable using name mangling
print(obj._MyClass__private_var)#Output: This is a private variable

#Accessing the private method using name mangling
obj._MyClass__private_method() #Output: This is a private method

f.dash()

f.section("Mangling Examples")

f.subsection("Example 1: Avoiding Naming Conflicts")

class Person:
    def __init__(self, name):
        self.__name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.__name = name #Use name mangling to differentiate
        self.__employee_id = employee_id

employee1 = Employee("John", 12345)
print(employee1._Person__name) #Access the__name attribute throgh name mangling
print(employee1._Employee__name) #Access the_name attribute in the Employee class

f.short_dash()

f.subsection("Example 2: Implementing Private Methods")

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def __process_transaction(self, amount):
        if amount < 0:
            raise ValueError("Transaction amount must be positive.")
        self.__balance += amount

    def deposit(self, amount):
        self.__process_transaction(amount)

    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Insufficient funds.")
        self.__process_transaction(-amount)

account = BankAccount("123456789", 1000)
account._BankAccount__process_transaction(500) #This works, but is not recommended

f.dash()
