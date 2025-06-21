import formatting as f

f.title("Independent Practice #18")
f.dash()

# --- Guest ---
print("\n--- Guest ---\n")

name_list = []  # Store guest names
filename = "guest.txt"

guest_name = input("Input your name: ").strip().title()  # Normalize input with proper capitalization

# Load existing names; handle new file creation if needed
try:
    with open(filename, "r") as file:
        name_list = [line.strip() for line in file if line.strip()]
    if guest_name not in name_list:  # Avoid duplicates
        name_list.append(guest_name)
    with open(filename, "w") as file:
        file.write("\n".join(name_list) + "\n")  # Overwrite with updated list
    print("\nCurrent Guest List:")
    print("\n".join(name_list))
except FileNotFoundError:
    with open(filename, "w") as file:
        file.write(guest_name + "\n")
    print("\nCurrent Guest List:")
    print(guest_name)

f.dash()

# --- Guest Book ---
print("\n--- Guest Book ---\n")

filename = "guest_book.txt"
checkin_list = []  # Track checked-in guests

# Infinite loop for guest check-in; exit on 'exit'
while True:
    guest_name = input("Please input the name of the guest (or type 'exit' to stop): ").strip().title()
    if guest_name.lower() == "exit":
        print("Exiting guest check-in.")
        break
    if guest_name not in checkin_list:  # Prevent duplicate check-ins
        checkin_list.append(guest_name)
        print(f"Welcome, {guest_name}! You have been checked in.")
    else:
        print(f"{guest_name} has already been checked in.")
    with open(filename, "a") as file:
        file.write(guest_name + "\n")  # Append new entry

# Display guest book contents
try:
    with open(filename, "r") as file:
        print("\nGuest Book Entries:")
        print(file.read())
except FileNotFoundError:
    print("\nGuest Book is empty.")

f.dash()

# --- Programming Poll ---
print("\n--- Programming Poll ---\n")

filename = "programming_poll.txt"
responses = []  # Store poll responses

# Collect responses until user exits
while True:
    response = input("Why do you like programming? (or type 'exit' to stop): ").strip()
    if response.lower() == "exit":
        print("Exiting programming poll.")
        break
    responses.append(response)
    with open(filename, "a") as file:
        file.write(response + "\n")

# Display poll results
try:
    with open(filename, "r") as file:
        print("\nProgramming Poll Responses:")
        print(file.read())
except FileNotFoundError:
    print("\nNo responses recorded yet.")

f.dash()
