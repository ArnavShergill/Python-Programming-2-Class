import formatting as f

f.title("Independent Practice #23")

f.dash()

f.section("Define Custom Exception Classes")

#Creating Custom Errors
class PopError(Exception):
    def __init__(self):
        print("Pop genre error occured")
    pass

class RockError(Exception):
    def __init__(self):
        print("Rock genre error occured")
    pass

class HipHopError(Exception):
    def __init__(self):
        print("Hip-Hop genre error occured")
    pass

class CountryError(Exception):
    def __init__(self):
        print("Country genre error occured")
    pass

f.dash()

f.section("Create a Function to Validate and Play a Song")

def data_validation(song):
    try:
        assert isinstance(song, dict), "Song is not a dictionary"
        #checks for if there are correct keys in the dictionary
        required_keys = ['Title', 'Artist', 'Genre']
        for key in required_keys:
            assert key in song, f"Missing required key: {key}"
        # Checks if the song genre is correct or not
        allowed_genres = ["Pop", "Rock", "Hip-Hop", "Country"]
        assert song['Genre'] in allowed_genres, "The genre of the song is incorrect or unsupported"
        # Checks if the title of the song has any banned words
        banned_title_words = ["World", "Tequila"]
        title_words = song["Title"].split()
        genre_to_error = {
            'Pop':PopError,
            'Rock':RockError,
            'Hip-Hop':HipHopError,
            'Country':CountryError
        }
        for word in title_words:
            if word == banned_title_words[1] or word == banned_title_words[0]:
                raise genre_to_error[song['Genre']]
    # Error Handling
    except AssertionError:
        print("The song is either not a dictionary or is missing a parameter")
    except (PopError, RockError, HipHopError, CountryError):
        print("This is the incorrect genre.")
    else:
        print(f"Now Playing: {song['Title']} by {song['Artist']} [{song['Genre']}]")
            

f.dash()

f.section("Prepare a List of Songs")

#Songs
Song1 = {
    "Title":"Hotel California",
    "Artist":"Eagles",
    "Genre":"Rock"
}

Song2 = {
    "Title":"Perfect",
    "Artist":"Ed Sheeran",
    "Genre":"Pop"
}

Song3 = {
    "Title":"Cowbell",
    "Artist":"ditro",
    "Genre":"Electronic"
}

Song4 = {
    "Title":"Tequila Sunrise",
    "Artist":"Eagles",
    "Genre":"Rock"
}

Song5 = {
    "Title":"Sh-Boom",
    "Artist":"The Chords",
    "Genre":"Country"
}

#List to Cycle Through
song_list = [Song1, Song2, Song3, Song4, Song5]

f.dash()

f.section("Loop Through the List of Songs")

for song in song_list:
    data_validation(song)

f.dash()
