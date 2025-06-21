def dash():
  print("\n--------------------------------\n")

print("--- Python 1 Review: Conditionals ---")

dash()

print("-- Understanding Inequality --\n")

# I did if num1 != num2 then it would be true otherwise it would be false in that order because of the way the instructions were written.
def are_different(num1, num2):
  """Returns true if num1 and num2 are different, false otherwise."""
  if num1 != num2:
    return True
  else:
    return False

print(are_different(1,2))
print(are_different(3,3))

dash()

print("-- Numerical Comparisons --\n")

def find_largest(num1, num2, num3):
  """An algorithm that goes through a list and finds which number is the greatest/largest."""
  #I had to make a list and add the numbers to it so that I could cycle through the elements in the list and use a comparison operator to find the largest number.
  #I did it this way so that I would not have to make a bunch of if-elif-else statements and make the code really inefficient and hard to read.
  num_list = []
  num_list.append(num1)
  num_list.append(num2)
  num_list.append(num3)
  largest = 0
  for num in num_list:
    if num > largest:
      largest = num
  return largest

print(find_largest(23,53,33))

dash()

print("-- Using And, Or, in If Statements --\n")

def in_range(num, start, end):
  """An algorithm for giving true or false if a number is in a user-specified range"""
  if (num >= start) and (num <= end):
    return True
  else:
    return False

print(in_range(5,2,7))
print(in_range(7,4,5))

dash()

print("-- Nexting and Compound Conditionals --\n")

def age_group(age):
  """An algorithm that tells you what age group you are in based on your age"""
  #Will work with any number
  if age < 13:
    return "Child"
  elif age >= 13 and age <= 19:
    return "Teenager"
  elif age >= 20 and age <= 65:
    return "Adult"
  elif age > 65:
    return "Senior"

print(age_group(10))
print(age_group(17))
print(age_group(30))
print(age_group(70))

dash()

print("-- Combining And, Or --\n")

def can_drive(age, vision_check):
  if (age >= 18) and (1 >= vision_check >= 0.8):
    return True
  else:
    return False

print(can_drive(23,0.9))
print(can_drive(17,0.6))

dash()