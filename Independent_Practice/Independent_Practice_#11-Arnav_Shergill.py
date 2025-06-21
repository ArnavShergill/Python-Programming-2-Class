import formatting as f

f.title("Independent Practice #11")

f.dash()

f.section("Pokemon")

class PokemonTrainer:
    def __init__(self, trainer_name):
        """sets the attributes of the instance"""
        self.trainer_name = trainer_name
        self.__pokemon_list = {}

    def get_pokemon_list(self):
        """will print out the contents of the list unless there are no contents to print out"""
        if not self.__pokemon_list:
            print("There are no Pokémon in this list")
        else:
                print(", ".join(f"{pokemon} (Level {level})" for pokemon, level in self.__pokemon_list.items()))

    def add_pokemon(self, pokemon_name, level):
        """Will let you add the Pokémon specified unless it's already in the dictionary"""
        if pokemon_name in self.__pokemon_list:
            print("This Pokémon is already in the Pokémon list")
        else:
            self.__pokemon_list[pokemon_name] = level
            print(f"{pokemon_name} added at level {level}")

    def remove_pokemon(self, pokemon_name):
        if pokemon_name in self.__pokemon_list:
            self.__pokemon_list.pop(pokemon_name)
            print(f"{pokemon_name} has been removed")
        else:
            print("This pokemon isn't in your pokemon list!")

Ash = PokemonTrainer("Ash")

Ash.add_pokemon("Pikachu", 10)
Ash.add_pokemon("Charizard", 25)
Ash.add_pokemon("Magikarp", 13)
Ash.add_pokemon("Raichu", 11)
Ash.add_pokemon("Charmander", 5)
Ash.add_pokemon("Bulbasaur", 21)
Ash.add_pokemon("Weedle", 12)
Ash.add_pokemon("Beedrill", 18)
Ash.add_pokemon("Watchog", 17)
Ash.add_pokemon("Kricketune", 24)

f.short_dash()

Ash.add_pokemon("Charizard", 25)

f.short_dash()

Ash.remove_pokemon("Frogadier")

f.short_dash()

Ash.remove_pokemon("Watchog")

f.short_dash()

print(Ash.get_pokemon_list())

f.dash()
