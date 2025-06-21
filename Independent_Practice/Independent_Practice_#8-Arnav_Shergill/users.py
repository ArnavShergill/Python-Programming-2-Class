class Users:
    # "__init__" method for the info for the class that sets each object apart
    def __init__(self, first_name, last_name, age, sibling_count, birthday, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sibling_count = sibling_count
        self.birthday = birthday
        self.hobby = hobby

    login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"\nAttmpts to login:\n{self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("\nThe login attempt count has reset to 0")

    # custom greeting for the user but isn't looped since couldn't figure out how to get the attributes from "__init__" and turn into loopable list
    def greet_user(self):
        print(f"The first name is:\n{self.first_name}\n")
        print(f"The last name is:\n{self.last_name}\n")
        print(f"The age is:\n{self.age}\n")
        print(f"The number of siblings are:\n{self.sibling_count}\n")
        print(f"The birthday is:\n{self.birthday}\n")
        print(f"The hobby is:\n{self.hobby}")
