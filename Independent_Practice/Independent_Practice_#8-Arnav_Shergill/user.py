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

class Privilege:
    def __init__(self, add_post, delete_post, ban_user):
        self.add_post = add_post
        self.delete_post = delete_post
        self.ban_user = ban_user

    def show_privileges( true_false1, true_false2, true_false3):
        privilege_dict = {"add post":true_false1, "delete post":true_false2, "ban user":true_false3}
        for key in privilege_dict:
            print(f"{key.title()}: {privilege_dict[key]}")

class Admin(Users):
    def admin_priv(self):
        Privilege.show_privileges(True, True, True)
