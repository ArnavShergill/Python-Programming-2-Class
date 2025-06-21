from users import Users

# Users class in the users file

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
