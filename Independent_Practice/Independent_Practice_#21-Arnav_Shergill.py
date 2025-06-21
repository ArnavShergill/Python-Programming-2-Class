import formatting as f
import random as r

f.title("Independent Practice #21")

f.dash()

f.section("K-Pop")

#list of names to be used later for output
member_names = ['RM', 'Jin', "Suga", "J-Hope", "Jimin", "V", "Jungkook"]

def member_albums(member_name, num_albums):
    """Will print out member name with album releases unless wrong input given"""
    try:
        assert num_albums > 0, "The number of albums released cannot be negative"
        assert isinstance(member_name, str), "The name was inputted incorrectly"
    except AssertionError:
        print("You have either entered a wrong number or wrong name.")
    else:
        f.short_dash()
        print(f"{member_name} has released {num_albums} number of albums\n")
    finally:
        print("Function member_albums has finished execution.")

# Cycles through names in the member_names list and outputs for each member.
for name in member_names:
    member_albums(name, r.randint(0, 15))

f.dash()

f.section("Cuisine")

# list of foods used for try except block and output
indian_food_menu = {
    'Samosa':10,
    "Butter Chicken":-200,
    "Tandoori Chicken":None,
    "Chana Masala":8,
    "Aloo Gobi":12,
    "Biryani":0,
    "Naan":2
}

def check_menu(menu):
    """will check if price is correct on menu else will error"""
    for key in menu:
        value = menu[key]
        try:
            if value == None:
                menu[key] = "Missing"
                continue
            elif value < 0:
                raise ValueError
        except ValueError:
            menu[key] = "Incorrect Food Price"
        else:
            menu[key] = "Correct Food Price"

    print("Here is a list of all our items and if they are correct.")
    for key in menu:
        value = menu[key]
        print(f"{key}: {value}")

check_menu(indian_food_menu)

f.dash()