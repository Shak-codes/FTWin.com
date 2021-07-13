import json

data = open('../data.json')
data = json.load(data)

def add_tournament():

    # Get tournament series name
    series_name = "BBB"
    #input("What is the name of the tournament series?\n")

    # Analyze data file to check if series_name is present, if not,
    # add to the tournament_series section in the data file

    # Obtain a list of all series present in data file
    all_series = data['data']['tournaments']['series']

    # Set x to value 0
    x = 0

    # Check if series_name present in datafile, update x if so
    for i in all_series:
        if str(i["name"]) == series_name:
            x = x + 1
    
    # If x has not been updated, add series_name to data file
    if x == 0:
        new_series = {
            "id": len(all_series) + 1,
            "name": series_name
        }

        data['data']['tournaments']['series'].append(new_series)

    # Get tournament edition
    edition = 1
    #input("What is the edition of the tournament series?\n")

    # Get tournament date
    date = "Jul 2 2021"
    #input("What was the date of the tournament\n")

    # Get tournament placing
    result = "1st"
    #input("What place did you get in the tournament?\n")

    # Get tournament stage data (IE. Swiss stage then Top Cut)
    stages_length = 2
    #int(input("How many stages did the tournament have?\n"))

    stages = []

    # store number of sets per tournament stage
    sets_per_stage = []

    # store name of each set in the tournament
    stage_round_names = []

    # store number of games played for each set
    stage_games = []

    tournament = []

    team_one = ""
    team_two = ""

    for stage in range(stages_length):

        # Get name of tournament stage
        current_stage = stage + 1
        name = "swiss"
        #input("What is the name of stage " + current_stage + " ?\n")
        stages.append(name)

        sets = 3
        #int(input("How many sets were in the " + stages[stage] + " stage?\n"))
        sets_per_stage.append(sets)

        idx = 0

        # Get name of each set in the stage of the tournament
        while (idx < sets_per_stage[stage]):
            round = idx + 1
            round_name = "Swiss Round 1"#input("What was round " + str(round) + " called?\n")
            stage_round_names.append(round_name)
            idx = round

        # Get number of games played for each set
        for i in range (sets_per_stage[stage]):
            game_count = 1#input("How many games did you play in " + str(stage_round_names[i]) + "?\n")
            stage_games.append(game_count)

        set = []
        for i in range (sets_per_stage[stage]):
            current_set = i + 1
            game = []
            set_weapons = []
            for j in range(int(stage_games[i])):
                game_id = j + 1
                map = "Inkblot"
                #input(stage_round_names[i] + " | Game " + str(game_id) + " Map name: ")
                mode = "Turf War"
                #input(stage_round_names[i] + " | Game " + str(game_id) + " Mode name: ")
                team = []
                game_weapons = []
                for k in range(2):
                    team_weapons = []
                    team_id = k + 1
                    team_name = "FTWin" + str(team_id)#input("Team name: ")

                    if team_id == 1:
                        team_one == team_name
                    else:
                        team_two == team_name

                    game_result = "WIN"
                    #input("Did " + str(team_name) + " win or lose?(ENTER WIN OR LOSS)")
                    score = "78"
                    #input(str(team_name) + " score")

                    # Array to store all player data
                    players = []

                    for player in range(4):

                        player_name = "Shak"#input("Player " + str(player) + " name: ")
                        player_weapon = "KSHOT"#input(str(player_name) + "'s weapon: ")

                        if (player_weapon not in team_weapons):
                            team_weapons.append(player_weapon)
                        if (player_weapon not in game_weapons):
                            game_weapons.append(player_weapon)
                        if (player_weapon not in set_weapons):
                            set_weapons.append(player_weapon)

                        player_paint = "1000"#input(str(player_name) + " paint: ")
                        player_kills = "5"#input(str(player_name) + " kills(assists included): ")
                        player_assists = "3"#input(str(player_name) + " assists: ")
                        player_deaths = "0"#input(str(player_name) + " deaths: ")
                        player_specials = "2"#input(str(player_name) + " deaths: ")

                        player_data = {
                            "id": player + 1,
                            "name": player_name,
                            "weapon": player_weapon,
                            "paint": player_paint,
                            "kills": player_kills,
                            "assists": player_assists,
                            "deaths": player_deaths,
                            "specials": player_specials
                        }

                        players.append(player_data)

                    team_data = {
                        "id": team_id,
                        "name": team_name,
                        "result": game_result,
                        "score": score,
                        "players": players,
                        "weapons": team_weapons
                    }
                    team.append(team_data)


                player_data = {"team": team}

                game_data = {
                    "id": game_id,
                    "map": map,
                    "mode": mode,
                    "player_data": player_data,
                    "weapons": game_weapons
                }

                game.append(game_data)
            
            set_data = {
                "id": current_set,
                "name": stage_round_names[i],
                "game_data": game,
                "weapons": set_weapons
            }

            set.append(set_data)

        tournament_data = {
            "id": current_stage,
            "name": name,
            "set_data": set
        }

        tournament.append(tournament_data)
    
    bracket = {"tournament_stages": tournament}

    new_data = {
        "bracket": bracket,
        "weapons": 5
        }
        
    individual_tournament = {
        "id": len(data['data']['tournaments']['individual_tournaments']) + 1,
        "name": series_name,
        "edition": edition,
        "date": date,
        "result": result,
        "data": new_data
    }
    
    data['data']['tournaments']['individual_tournaments'].append(individual_tournament)

    json_object = json.dumps(data, indent = 4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    
    print("Completed")
