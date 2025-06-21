import my_module

def my_function():
    print("Hello, world!")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(2, 3)
    print(result)

def say_hello():
    print("Hello, world!")

print("This code is executed when the module is imported.")

if __name__ == "__main__":
    print("This code is executed when the module is run as the main program")
