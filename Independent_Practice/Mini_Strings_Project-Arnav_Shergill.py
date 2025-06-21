import formatting as f

f.clear_console()

f.title("Mini Strings Project")

f.dash()

# Menu to display
main_menu = {
    1: "Encode a message",
    2: "Decode a message",
    3: "Reverse a message",
    4: "Display ASCII values of a message",
    5: "Exit"
}

# Function to display the menu
def menu():
    """prints the main menu when called on"""
    for item in main_menu:
        print(f"{item}: {main_menu[item]}")
    f.short_dash()

# Message Encoder
def message_encode(message, key: int) -> str:
    """encodes a message"""
    new_message = []
    for char in message:
        if isinstance(char, str):
            new_char = ord(char) + key
            new_message.append(chr(new_char))
        else:
            pass
    return "".join(new_message)

# Message Decoder
def message_decode(message, key: int) -> str:
    """Decodes a message"""
    return message_encode(message, -key)

# Reverse Message
def reverse_message(message: str) -> str:
    """Reverses a message"""
    return message[::-1]

# ASCII values
def ASCII_values(message: str):
    """Gives the ASCII values for each character in the message"""
    for char in message:
        print(f"{char}: {ord(char)}")

# Counter used to get out of while loop
counter = 0
while counter != 1:
    # Main loop to display everything
    # Nothing will display if this doesn't work.
    menu()
    user_choice = input("What would you like to do?\n")
    try:
        user_choice = int(user_choice)  # Convert input to integer
        if user_choice == 1:  # Changed to integer comparison
            user_message = input("\nPlease input a string to encode: ")
            user_key = int(input("Please enter an integer: "))
            print(message_encode(user_message, user_key))
            f.user_continue()
        elif user_choice == 2:
            user_message = input("\nPlease input a string to decode: ")
            user_key = int(input("Please enter an integer: "))
            print(message_decode(user_message, user_key))
            f.user_continue()
        elif user_choice == 3:
            user_message = input("What string would you like to reverse?\n")
            print(reverse_message(user_message))
            f.user_continue()
        elif user_choice == 4:
            user_message = input("What would you like to convert to ASCII values?\n")
            ASCII_values(user_message)
            f.user_continue()
        elif user_choice == 5:
            print("Thanks for visiting.")
            counter = 1
            break
    except ValueError:
        print("You did not enter the right value. Please try again.")
        f.user_continue()

f.dash()