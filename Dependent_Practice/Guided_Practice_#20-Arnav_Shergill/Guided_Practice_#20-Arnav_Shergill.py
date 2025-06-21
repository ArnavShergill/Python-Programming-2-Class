import formatting as f

f.title("Guided Practice #20")

f.dash()

f.section("Handling the FileNotFoundError Exception")

f.subsection("Alice in Wonderland")

filename = 'alice.txt'

try:
    with open(filename, encoding = "utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

f.dash()

f.section("Analyzing Text")

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} dose not exist.")
else:
    #Count trhe approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

f.dash()

f.section("Working wiwth Multiple Files")

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        #Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

f.short_dash()

filenames = ['alice.txt', 'sidhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

f.dash()

f.section("Failing Silently")

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        #Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'sidhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

f.dash()
