import formatting as f

f.title("Independant Practice 1")

f.dash()

f.section("Exercise 1: Concord Attractions")

Concord_Attractions = {"NASCAR Hall of Fame":2, "Great Wolf Lodge":3, "SEA LIFE Charlotte - Concord":5, "Frank Liske Park":4, "Concord Mills":1}

#This prints the list in a nice-looking output
for x in sorted(Concord_Attractions):
    print(x, ":", Concord_Attractions[x])

f.dash()

f.section("Exercise 2: Tourist Spots")

location_information = {} #dictionary

# I made the algorithm work without a dictionary, but for the sake of the assignment, I integrated a system where the user would specify how many places they would add, and then every time the loop iterates, it adds the new variables to the dictionary
def location_dictionary():
    total_fees = 0
    """Asks the user for how many locations they want to put in, then asks the user the location and price questions the amount of times they specified"""
    user_input = int(input("How many locations do you want to input? "))
    loop_count = 0
    while loop_count < user_input:
        spot = input("\nEnter the location name: ")
        fees = int(input("Enter the location fees: "))
        location_information.update({spot: fees})
        total_fees = total_fees + fees
        loop_count+=1

    print(f"\nYour trip costed: ${total_fees}.\n")

location_dictionary()

f.dash()

f.section("Exercise 3: Restaurant Rating")

Concord_Restaurants = {'Johnny Rogers':4.0, 'Birritaco':4.5, "Lil Papi's International Deli":5.0, 'The Smoke Pit':4.5, "Havana Carolina":4.0, "Benny DaCorsa's":4.0, "La Auténtica":4.7}

#chose f-string because of readability and easy to code
user_search = input("What is a restaurant that you want to go to? ")
if user_search in Concord_Restaurants:        
    print(f"The rating for {user_search} is {Concord_Restaurants[user_search]}.")
else:
    print(f"There is no restaurant named {user_search} in Concord, North Carolina")


f.dash()
