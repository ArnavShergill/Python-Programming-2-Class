import formatting as f

f.title("Independent Practice #27")

f.dash()

f.clear_console()

f.section("Task 1: Unique Sports List")

high_school_sports = ["Cross Country Mountain Biking", "Cross Country Mountain Biking", "Wrestling", "Soccer", "Football", "Soccer", "Tennis", "Baseball", "Volleyball", "Golf", "Robotics", "Track & Field", "Softball", "Swimming", "Lacrosse", "Hockey"]

hss = set(high_school_sports)
print(", ".join(hss))

f.dash()

f.section("Task 2: Club Membership Intersection and Union")

Science_Club = {"Arnav", "Pranav", "Saketh", "Mahee", "Amshul", "Arhum", "Faiz", "Sukrut", "Srithan", "Alex"}
Math_Club = {"Arnav", "John", "Jordan", "Alexander", "Matthew", "Arhum", "Sukrut", "Gavin", "Anika", "Faiz"}
Common_People = Science_Club.intersection(Math_Club)
print(", ".join(Common_People))

f.dash()

f.section("Task 3: Exclusive Membership (Set Difference)")

Science_Club = {"Arnav", "Pranav", "Saketh", "Mahee", "Amshul", "Arhum", "Faiz", "Sukrut", "Srithan", "Alex"}
Math_Club = {"Arnav", "John", "Jordan", "Alexander", "Matthew", "Arhum", "Sukrut", "Gavin", "Anika", "Faiz"}
Set_Difference = Science_Club - Math_Club
print(", ".join(Set_Difference))

f.dash()

f.section("Task 4: Social Media Apps and Set Membership Testing")

social_media = {"Discord", "Snapchat", "Instagram", "Youtube"}

user_social = input("What Social Media do you think students use?\n").title()

if user_social in social_media:
    print("\nThat is correct!")
else:
    print("\nThat is incorrect.")

f.dash()

f.section("Task 5: Set Comprehension with Filtering")

long_hss = set(map(lambda x: x if len(x) > 6 else "", hss))
long_hss.remove("")
print(", ".join(sorted(long_hss)))

f.dash()
