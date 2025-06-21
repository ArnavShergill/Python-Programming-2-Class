from formatting import *

title("Python 1 Review: Tuples")

section("Creating Tuples from User Input")

subsection("Task 1")

# I didn't understand what the instructions said about slicing in a tuple, so that is why I took the variables into tuple method
student_name = input("Enter student name: ")
student_age = input("Enter student age: ")
student_favorite_subject = input("Enter student's favorite subject: ")
student_info = (student_name, student_age, student_favorite_subject)

print("\n", formatted_list(student_info))

short_dash()

subsection("Task 2")

#used the same method as Task 1 because I was too lazy to try to learn how to slice a tuple
teacher_name = input("Enter teacher name: ")
teacher_room_number = input("Enter teacher room number: ")
teacher_subject = input("Enter teacher subject: ")
teacher_info = (teacher_name, teacher_room_number, teacher_subject)
print("\n", formatted_list(teacher_info))

dash()

section("Slicing Tuples")

subsection("Task 1")

#uses indexes of the tuple instead of the variables because this assignment is about tuples, not variables
print(f"Teacher Name: {teacher_info[0]}")
print(f"Teacher Room Number: {teacher_info[1]}")
print(f"Teacher  Subject: {teacher_info[2]}")

short_dash()

subsection("Task 2")

#Used f-string instead of other ways of string formatting because it is the most understandable and straightforward. It is also really easy to work with.
print(f"Student Name: {student_info[0]}")
print(f"Student Age: {student_info[1]}")
print(f"Student Favorite Subject: {student_info[2]}")

dash()

section("Using Tuples in Functions")

subsection("Task 1")

#just printed the value of the elements instead of printing in an f-string with a string as there was no specifications.
def print_teacher_info(teacher_list):
    """Takes info from teacher_info list and prints it"""
    print(teacher_list[0])
    print(teacher_list[1])
    print(teacher_list[2])

print_teacher_info(teacher_info)

short_dash()

subsection("Task 2")

#do docstrings count as comments?
def print_student_info(student_list):
    """Takes info from student_info list and prints it"""
    print(student_list[0])
    print(student_list[1])
    print(student_list[2])

print_student_info(student_info)

dash()
