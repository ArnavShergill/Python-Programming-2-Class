import formatting as f
import platform
import math as m
import sys as s
from my_module import my_function

f.title("Guided Practice #16")

f.dash()

f.section("Platform Examples")

f.subsection("Retrieving the Operating System Name")

print(platform.system())

f.short_dash()

f.subsection("Retrieving the Python Version")

print(platform.python_version())

f.short_dash()

f.subsection("Retrieving the Machine's Processor Type")

print(platform.processor())

f.short_dash()

f.subsection("Retrieving Information about the Machine's Network")

print(platform.node())

f.short_dash()

f.subsection("Retrieving information about the Machine's Architecture")

print(platform.architecture())

f.short_dash()

f.subsection("Retrieving Information about Python's Implementation")

print(platform.python_implementation()) #Output: CPython

f.dash()

f.section("dir() Function")

f.subsection("Examining a Module's Contents")

print(dir(m))

f.short_dash()

f.subsection("Examining an Object's Attributes")

string = "hello Sushi"
print(dir(string))

f.short_dash()

f.subsection("Examining The Current Scope")

def my_function():
    x = 5
    print(dir())
my_function()

f.dash()

f.section("Sys.path Variable")

print(s.path)

f.short_dash()

f.section("Python_version_tuple()")

version_tuple = s.version_info

print(version_tuple)

print("Python version:", ",".join(map(str, version_tuple)))

f.dash()

f.section("Directory")

my_function()

f.dash()
