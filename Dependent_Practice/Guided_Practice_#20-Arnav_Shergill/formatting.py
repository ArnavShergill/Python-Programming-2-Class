import time
import os
import sys

os.system("rm -r __pycache__")

def slow_print(text, delay=0.05, pause = 1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(pause)
    print()

def show_menu(menu):
    for key, value in menu.items():
        slow_print(f"{key}: {value}")

    global user_input
    user_input = input("\nWhat would you like to do?\n ").lower().strip()

def title(title_name):
    slow_print(f"---- {title_name} ----")

def section(section_name):
    slow_print(f"--- {section_name} ---\n")

def subsection(subsection_name):
    slow_print(f"-- {subsection_name} --\n")

def dash():
    print("\n----------------------------------\n")
    time.sleep(1)

def formatted_list(list_name):
    return(", ".join(list_name))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def user_continue():
    print("Press Enter to Continue")
    input()
    clear_console()

if __name__ == "__main__":
    print("This is a module. Please run the main file.")
