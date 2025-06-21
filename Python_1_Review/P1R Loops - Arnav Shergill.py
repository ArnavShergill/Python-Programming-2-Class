def dash():
  print("\n--------------------------------\n")

print("---- Python 1 Review: Loops ----")

dash()

print("--- Basic For Loops ---\n")

# This algorithm takes a while with the really big numbers. but then again... it's python.
def sum_of_n(n):
  """iterates through a range of numbers from 1 to n and adds them together"""
  sum = 0
  for i in range(0, n):
    sum += n
  
  return sum

print(sum_of_n(999999))

dash()

print("--- Basic While Loops ---\n")

#algorithm is versatile with any range of numbers
def countdown(n):
  """iterates through a range of numbers from n to 0 and prints them"""
  counter = n
  while counter > 0:
    print(counter)
    counter -= 1

print(countdown(10))

dash()

print("--- Combining for Loops with Functions ---\n")

# Do docstrings count as comments? I hope so.
def factorial(n):
  """checks to see if n is a factorial"""
  if n == 0:
    return "the factorial of 0 is 1"
  elif n < 0:
    return "There is no factorial for negative numbers"
  else:
    product = 1
    for i in range(1, n):
      product *= i
  return product

print(factorial(999))

dash()

print("--- Using Flags with While Loops ---\n")

def is_prime(n):
  """checks if n is a prime number or not"""
  #I don't really understand this logic as I didn't know what flags were until now.
  found_divisor = False
  i = 2
  if n <=1:
    return False

  while i < n and not found_divisor:
    if n % i == 0:
      found_divisor = True
    i += 1
  return not found_divisor

print(is_prime(2))
print(is_prime(100))