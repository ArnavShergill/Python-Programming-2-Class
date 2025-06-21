def section(section_name):
    print(f"--- {section_name} ---\n")

def short_dash():
    print("\n----------------------------------\n")

def dash():
    print("\n-------------------------------------------------------------------------------------------------------\n")

def main():
    print("\n---- Mini Misc Project ----")
    dash()

    section("Task 1: Dataset Creation")

    players = [
        {'name': 'Scottie Scheffler',    'country': 'USA', 'score': 271},  # 17 under par
        {'name': 'Rory McIlroy',         'country': 'NIR', 'score': 272},  # 16 under par
        {'name': 'Cameron Smith',        'country': 'AUS', 'score': 272},  # 16 under par
        {'name': 'Justin Thomas',        'country': 'USA', 'score': 273},  # 15 under par
        {'name': 'Collin Morikawa',       'country': 'USA', 'score': 274},  # 14 under par
        {'name': 'Viktor Hovland',        'country': 'NOR', 'score': 275},  # 13 under par
        {'name': 'Xander Schauffele',     'country': 'USA', 'score': 275},  # 13 under par
        {'name': 'Hideki Matsuyama',     'country': 'JPN', 'score': 276},  # 12 under par
        {'name': 'Dustin Johnson',       'country': 'USA', 'score': 277},  # 11 under par
        {'name': 'Patrick Reed',         'country': 'USA', 'score': 278},  # 10 under par
        {'name': 'Sergio Garcia',        'country': 'ESP', 'score': 279},  # 9 under par
        {'name': 'Jordan Spieth',        'country': 'USA', 'score': 280},  # 8 under par
        {'name': 'Brooks Koepka',        'country': 'USA', 'score': 280},  # 8 under par
        {'name': 'Im Sung-jae',          'country': 'KOR', 'score': 280},  # 8 under par
        {'name': 'Bubba Watson',         'country': 'USA', 'score': 281},  # 7 under par
        {'name': 'Jason Day',            'country': 'AUS', 'score': 282},  # 6 under par
        {'name': 'Will Zalatoris',       'country': 'USA', 'score': 282},  # 6 under par
        {'name': 'Tony Finau',           'country': 'USA', 'score': 283},  # 5 under par
        {'name': 'Matthew Wolff',        'country': 'USA', 'score': 283},  # 5 under par
        {'name': 'Keegan Bradley',       'country': 'USA', 'score': 284}   # 4 under par
    ]

    for item in players:
        # prints out list of dictionaries with the players' info in a nice, formatted way
        print(f"{item['name']} is from {item['country']} and has a score of {item['score']}")
    dash()

    section("Task 2: Extract Unique Countries")
    # Prints the country of each player (with no duplicates)
    player_country = set(map(lambda x: x["country"], players))
    print("\n".join(player_country))
    dash()

    section("Task 3: Retrieve Player Names")
    # Prints out the names of each player
    player_name = set(map(lambda x: x['name'], players))
    print("\n".join(player_name))
    dash()

    section("Task 4: Filter Top Performers")
    # Prints out the golfers that perform well
    top_performers = list(filter(lambda x: x["score"] < 280, players))
    for player in top_performers:
        print(f"{player['name']}: {player['score']}")
    dash()

    section("Task 5: Calculate 'Under Par' Scores using List Comprehension")
    # Calculates and prints the under par for each player
    players = [dict(player, under_par = 288 - player['score']) for player in players]
    for player in players:
        print(f"{player['name']}: Score = {player['score']}, Under Par = {player['under_par']}")
    dash()

    section("Task 6: Sort Players by 'Under Par'")
    # Sorts the players based on "Under Par"
    sorted_players = sorted(players, key=lambda x: x['under_par'], reverse=True)
    for player in sorted_players:
        print(f"{player['name']}: Under Par = {player['under_par']}, Score = {player['score']}")
    dash()

    section("Task 7: Identify Exceptional Performers Using Set Comprehension")
    # Uses set comprehension to identify exceptional performers
    exceptional_players = {player['name'] for player in players if player['under_par'] > 15}
    if exceptional_players:
        print("\n".join(exceptional_players))
    else:
        print("No players with under par score greater than 15")
    dash()

    section("Task 10: Testing & Edge Cases")
    # Will filter out which players have missing scores if there are any, and will find any duplicate names if there are any
    missing_scores = [player['name'] for player in players if 'score' not in player or player['score'] is None]
    if missing_scores:
        print(f"Warning: Missing scores for players: {', '.join(missing_scores)}")
    else:
        print("All players have valid scores")
    
    names = [player['name'] for player in players]
    # I don't know if we ever learned .count() in class, but I did look through w3schools and found this method
    # thought that it would be really useful in this use case scenario
    duplicates = set(name for name in names if names.count(name) > 1)
    if duplicates:
        print(f"Warning: Duplicate player names found: {', '.join(duplicates)}")
    else:
        print("No duplicate player names found")
    dash()

if __name__ == "__main__":
    main()
