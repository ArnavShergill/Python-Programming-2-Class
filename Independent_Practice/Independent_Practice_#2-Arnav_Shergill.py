import formatting as f

f.title("Independent Practice #2")

f.dash()

f.section("Task 1")

favorite_things = {"foods":input("Input three of your favorite foods separated by a comma and a space: ").split(", "), "hobbies":input("Input three of your favorite hobbies separated by a hyphen: ").split("-")}

print(favorite_things["foods"])
print(favorite_things["hobbies"])

f.dash()

f.section("Task 2")

student_info = {"first name":"Arnav", "last name":"Shergill", "grade":11}

print(", ".join(student_info.keys()))
for value in student_info.values():
  print(value)

unknown_key = student_info.get("favorite sport")

if unknown_key is None:
  print("No favorite sport found")

student_info.update({"favorite sport":"Mountain Biking"})

print(", ".join(student_info.keys()))

f.dash()
