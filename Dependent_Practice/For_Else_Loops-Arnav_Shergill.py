import formatting as f

f.title("For Else Loops")

f.section("Syntax of For/Else Loops")

iterable = []

for item in iterable:
    print("hello".title())
    #code block executed for each item
    #Optional break statement can terminate the loop early
else:
    hello = 'greeting'
    #Code block executed if the loop completes without encountering a break

f.dash()

f.section("Example 1: If the Number is Found During the Loop")

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print("Found 3!")
        break #break loop early
else:
    print("Number 3 not found.") #This won't run if 3 is found

print("Loop finished")

f.dash()

f.section("Example 2: If the Key is Not Found")

# Dictionary with student names as tuple keys
student_grades = {
    "Mia": 85,
    "Agastya": 92,
    "Helena": 78,
    "Atul": 88
}

search_name = "Thanmaya"

# Searching for a student using for/else
for name in student_grades:
    if name == search_name:
        print(f"Found {search_name} with grade: {student_grades[name]}")
        break
else:
    print(f"{search_name} not found.")

f.dash()
