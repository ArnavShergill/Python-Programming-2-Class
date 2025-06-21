import formatting as f
import random as r

f.title("Independent Practice #15")

f.dash()

f.section("Task 1: Sample() & Choice()")

print(r"""
                                      ---- Task X ----
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠷⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⣶⣦⣼⣿⣿⣿⣿⣿⣿⡟⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣾⣿⣿⣿⣿⣿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⣿⡟⣹⡟⣴⢻⣷⠘⠿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⡿⠐⢋⣴⣋⣯⣽⣷⣦⣤⠤⣾⣿⣿⣿⣿⣿⣿⠻⢿⣿⣿⣿⣿⣿⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣿⣒⡻⠟⣿⣨⣿⠉⠉⠐⣲⣿⣿⣿⣿⣿⣿⣿⠀⠀⠉⠙⠛⠻⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣷⡤⣢⢹⠉⣣⣠⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣦⣤⣤⣬⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣿⣿⢿⣡⡆⡤⣭⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠛⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣽⣿⣷⣅⣿⣷⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠛⠈⠙⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⠏⠙⠿⣿⣿⣿⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⢹⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡿⠃⠀⠀⠀⠈⠙⠋⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣷⠀⠀⠀⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣄⠘⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣧⠸⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠙⠻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      """) 

def sample_and_choice(list_name):
    """takes sample from list_name and choice from sample and then prints in a user_friendly output"""
    sample = r.sample(list_name, k = 5)
    choice = r.choice(sample)
    print(f"The sample taken is:\n{'\n'.join(samp for samp in sample)}\nand the choice from the sample is:\n{choice}")

enemies = ["Bokoblin", "Moblin", "Lizalfos", "Lynel", "Hinox", "Wizzrobe", "Guardian", "Yiga Footsoldier", "Talus", "Stalnox", "Hinox (Stalnox)", "Molduga", "Stalker Guardian", "Hyrulean Soldier (Enemy)", "Yiga Blademaster", "Stone Talus", "Igneo Talus", "Frost Talus", "Thunderblight Ganon", "Windblight Ganon", "Waterblight Ganon", "Fireblight Ganon", "Calamity Ganon", "Master Kohga", "Dark Beast Ganon"]
weapons = ['Traveler\'s Sword', 'Soldier\'s Broadsword', 'Knight\'s Claymore', 'Boko Club', 'Spiked Boko Club', 'Dragonbone Boko Club', 'Lizal Boomerang', 'Lizal Forked Boomerang', 'Lizal Tri-Boomerang', 'Guardian Sword', 'Guardian Sword+', 'Guardian Sword++', 'Ancient Short Sword', 'Ancient Sword', 'Rusty Broadsword', 'Royal Broadsword', 'Forest Dweller\'s Sword', 'Zora Sword', 'Feathered Edge', 'Gerudo Scimitar', 'Moonlight Scimitar', 'Scimitar of the Seven', 'Eightfold Blade', 'Edge of Duality', 'Serpentine Spear']
characters = ["Link","Zelda","Mipha","Daruk","Revali","Urbosa","Impa","Purah","Robbie","Sidon","Yunobo", "Teba","Riju","Kass", "Hestu","Master Kohga","Monk Maz Koshia","King Rhoam","Princess Zelda", "Great Deku Tree","King Dorephan","Sergeant Link","Paya", "Beedle","Bolson","Hudson", "Greyson"]
locations = ["Great Plateau","Hyrule Field","Faron Woods","Eldin Mountains","Gerudo Desert", "Hebra Mountains", "Tabantha Frontier","Akkala Highlands","Lanayru Wetlands", "Mount Lanayru","Zora's Domain","Kakariko Village", "Hateno Village","Rito Village",    "Gerudo Town", "Tarrey Town","Lurelin Village","Satori Mountain", "Shrine of Resurrection","Hylian River","Lake Hylia","Death Mountain", "Lost Woods","Korok Forest", "Akala Island","Eventide Island","Ganondorf's Castle", "The Master Sword"]

list_of_lists = [enemies, weapons, characters, locations]

f.short_dash()

# Since all of the Examples are the same, it would be more efficient to run it in a for loop

for index, example in enumerate(list_of_lists,1):
    f.subsection(f"Example {index}")
    sample_and_choice(example)
    if index != 4:
        f.short_dash()
    else:
        f.dash()

f.section("Task 2: Seed()")

for index, example in enumerate(list_of_lists, 1):
    f.subsection(f"Example {index}")
    r.seed(100)
    print(r.random())
    print()
    sample_and_choice(example)
    if index != 4:
        f.short_dash()
    else:
        f.dash()

"""The for loop will loop 4 times, and every time it loops, it will print a value from r.random and then print the sample and choice taken by the function that was defined at the top of the file
Then, if the index is less than four, it will do one function defined in formatting, else it will do the other function in the formatting file. The if else is just for making the output look nice.
Task 1 is the same but without the r.seed and r.random"""
