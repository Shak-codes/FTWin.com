import json

data = open('../data.json')
data = json.load(data)


def add_tournament():

    # Get tournament series name
    series_name = "GGG"#input("What is the name of the tournament series?\n")

    # Get tournament edition
    edition = 1#input("What is the edition of the tournament series?\n")

    # Get tournament date
    date = "Jul 2 2021"#input("What was the date of the tournament\n")

    # Get tournament placing
    result = "1st"#input("What place did you get in the tournament?\n")

    # Get tournament stage data (IE. Swiss stage then Top Cut)
    stages_length = 2#int(input("How many stages did the tournament have?\n"))
    stages = []

    # number of sets per tournament stage
    sets_per_stage = []

    # name of each set in the tournament
    stage_round_names = []

    # number of games played for each set
    stage_games = []

    tournament = []

    for stage in range(stages_length):

        # Get name of tournament stage
        current_stage = stage + 1
        name = "swiss"#input("What is the name of stage " + current_stage + " ?\n")
        stages.append(name)

        sets = 3#int(input("How many sets were in the " + stages[stage] + " stage?\n"))
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
            for j in range(int(stage_games[i])):
                game_id = j + 1
                map = "Inkblot"#input(stage_round_names[i] + " | Game " + str(game_id) + " Map name: ")
                mode = "Turf War"#input(stage_round_names[i] + " | Game " + str(game_id) + " Mode name: ")
                team = []
                for k in range(2):
                    team_id = k + 1
                    team_name = "FTWin" + str(team_id)#input("Team name: ")
                    game_result = "WIN" #input("Did " + str(team_name) + " win or lose?(ENTER WIN OR LOSS)")
                    score = "78"#input(str(team_name) + " score")
                    players = []
                    weapons = []
                    paint = []
                    kills = []
                    assists = []
                    deaths = []
                    specials = []
                    for player in range(4):
                        player_name = "Shak"#input("Player " + str(player) + " name: ")
                        players.append(player_name)
                        player_weapon = "KSHOT"#input(str(player_name) + "'s weapon: ")
                        weapons.append(player_weapon)
                        player_paint = "1000"#input(str(player_name) + " paint: ")
                        paint.append(player_paint)
                        player_kills = "5"#input(str(player_name) + " kills(assists included): ")
                        kills.append(player_kills)
                        player_assists = "3"#input(str(player_name) + " assists: ")
                        assists.append(player_assists)
                        player_deaths = "0"#input(str(player_name) + " deaths: ")
                        deaths.append(player_deaths)
                        player_specials = "2"#input(str(player_name) + " deaths: ")
                        specials.append(player_specials)

                    team_data = {
                        "id": team_id,
                        "name": team_name,
                        "result": game_result,
                        "score": score,
                        "players": players,
                        "weapons": weapons,
                        "paint": paint,
                        "kills": kills,
                        "assists": assists,
                        "deaths": deaths,
                        "specials": specials
                    }
                    team.append(team_data)


                player_data = {"team": team}

                game_data = {
                    "id": game_id,
                    "map": map,
                    "mode": mode,
                    "player_data": player_data
                }

                game.append(game_data)
            
            set_data = {
                "id": current_set,
                "name": stage_round_names[i],
                "game_data": game,
            }

            set.append(set_data)

        tournament_data = {
            "id": current_stage,
            "name": name,
            "set_data": set
        }

        tournament.append(tournament_data)
    
    bracket = {"tournament_stages": tournament}

    new_data = {"bracket": bracket}
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
