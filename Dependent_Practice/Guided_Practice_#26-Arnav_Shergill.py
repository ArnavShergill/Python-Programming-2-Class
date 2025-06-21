import formatting as f

f.title("Guided Practice #26")

f.dash()

my_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in my_list]
print(squared_list)

f.short_dash()

my_list = [1, 2, 3, 4, 5]
even_list = [x for x in my_list if x % 2 == 0]
print(even_list)

f.short_dash()

my_list = [[1,2], [3, 4], [5, 6]]
flat_list = [num for sublist in my_list for num in sublist if num % 2 == 0]
print(flat_list)

f.dash()

f.section("Other Comprehensions")

f.subsection("List Comprehensions")

squares = [i*i for i in range(1,6)]
print(squares) # Output: [1, 4, 9, 16, 25]

f.short_dash()

f.subsection("Set Comprehension")

squares_set = {i*i for i in range(1,6)}
print(squares_set) # Output: {1, 4, 9, 16, 25}

f.short_dash()

f.subsection("Dictionary Comprehension")

word = "Hello"
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts) # Output: {'h': 1, 'e':1, 'l':2, 'o':1}

f.short_dash()

f.subsection("String Comprehension")

word = "hello"
vowels = ''.join([char for char in word if char in 'aeiou'])
print(vowels) # Output: 'eo'

f.dash()

f.section("Lambdas")

multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)

f.short_dash()

my_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, my_list))
print(squared_list)

f.dash()

f.section("Self-Defined Functions wtih Lambdas")

def apply_operation(operation, x, y):
    return operation(x,y)

result = apply_operation(lambda x,y: x + y, 3, 4)
print(result)

f.dash()

f.section("map() & filter() Functions")

def square(x):
    return x ** 2

my_list = [1, 2, 3, 4, 5]
squared_list = list(map(square, my_list))
print(squared_list)

f.short_dash()

def is_even(x):
    return x % 2 == 0

my_list = [1, 2, 3, 4, 5]
even_list = list(filter(is_even, my_list))
print(even_list)

f.dash()

f.section("Filter Function")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(filtered_numbers)

f.dash()

f.section("Filter Function Examples")

f.subsection("Example 1")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)

f.short_dash()

f.subsection("Example 2")

words = ['apple', 'banana', 'ornage', 'kiwi', 'peach']
filtered_words = list(filter(lambda x: len(x) < 5, words))
print(filtered_words)

f.short_dash()

f.subsection("Example 3")

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
filtered_numbers = tuple(filter(lambda x: x > 5, numbers))
print(filtered_numbers)

f.short_dash()

f.subsection("Example 4")

numbers = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
filtered_numbers = dict(filter(lambda x: x[1] % 2 == 0, numbers.items()))
print(filtered_numbers)

f.dash()

f.section("Map Function")

strings = ['apple', 'banana', 'cherry']
lengths = map(len, strings)
print(list(lengths)) # Output: [5, 6, 6]

f.short_dash()

f.subsection("Example 1")

# Define the function to square a number
def square(x):
    return x ** 2

# Define the list of numbers to square
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each number in the list
squared_numbers = map(square, numbers)

# Convert the map object to a list and prin tthe result
print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]

f.short_dash()

f.subsection("Example 2")

# Define the list of strings
strings = ['apple', 'banana', 'cherry']

# Use map() to apply the upper() method to each string in the list
uppercase_strings = map(str.upper, strings)

#Convert the map object t oa list and print the result
print(list(uppercase_strings)) # Output: ['APPLE', 'BANANA', 'CHERRY']

f.short_dash()

f.subsection("Example 3")

# Define the list of numbers
numbers = [1, 2, 3, 4, 5]

#Use map() to apply a lambda function to each number in the list
result = map(lambda x: x * 2 + 1, numbers)

# Convertt the map object to a list and print the result
print(list(result)) # Output: [3,5, 7, 9, 11]

f.dash()
