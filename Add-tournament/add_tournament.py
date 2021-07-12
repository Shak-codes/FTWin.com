import json

data = open('data.json')
data = json.load(data)

##print(data['data']['tournaments']['individual_tournaments'])

def add_tournament():

    # Get tournament series name
    series_name = input("What is the name of the tournament series?\n")

    # Get tournament edition
    edition = input("What is the edition of the tournament series?\n")

    # Get tournament date
    date = input("What was the date of the tournament\n")

    # Get tournament placing
    result = input("What place did you get in the tournament?\n")

    # Get tournament stage data (IE. Swiss stage then Top Cut)
    stages_length = int(input("How many stages did the tournament have?\n"))
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
        current_stage = str(stage + 1)
        name = input("What is the name of stage " + current_stage + " ?\n")
        stages.append(name)

        sets = int(input("How many sets were in the " + stages[stage] + " stage?\n"))
        sets_per_stage.append(sets)

        idx = 0

        # Get name of each set in the stage of the tournament
        while (idx < sets_per_stage[stage]):
            prefix_count = int(input("How many rounds share the same prefix?(out of " + str(sets_per_stage[stage] - idx) + ")? \n"))
            prefix = input("What is the name of the prefix?\n")
            for i in range (prefix_count):
                round_name = prefix + " " + input("What round did you play?\n")
                stage_round_names.append(round_name)
                idx = idx + 1

        # Get number of games played for each set
        for i in range (sets_per_stage[stage]):
            game_count = input("How many games did you play in " + str(stage_round_names[i]) + "?\n")
            stage_games.append(game_count)

        set = []
        for i in range (sets_per_stage[stage]):
            current_stage = i + 1
            result = input("Set " + str(i) + " result\n")
            set_score = input("Set score\n")
            game = []
            for j in range(int(stage_games[i])):
                game_id = j + 1
                map = input("Map name: ")
                mode = input("Mode name: ")
                game_score = input("Game score: ")
                team = []
                for k in range(2):
                    team_id = k + 1
                    team_name = input("Team name: ")
                    players = []
                    weapons = []
                    paint = []
                    kills = []
                    assists = []
                    deaths = []
                    for player in range(4):
                        player_name = input("Player " + str(player) + " name: ")
                        players.append(player_name)
                        player_weapon = input("Player " + str(player) + " weapon: ")
                        weapons.append(player_weapon)
                        player_paint = input("Player " + str(player) + " paint: ")
                        paint.append(player_paint)
                        player_kills = input("Player " + str(player) + " kills: ")
                        kills.append(player_kills)
                        player_assists = input("Player " + str(player) + " assists: ")
                        assists.append(player_assists)
                        player_deaths = input("Player " + str(player) + " deaths: ")
                        deaths.append(player_deaths)

                    team_data = {
                        "id": team_id,
                        "name": team_name,
                        "players": players,
                        "weapons": weapons,
                        "paint": paint,
                        "kills": kills,
                        "assists": assists,
                        "deaths": deaths
                    }
                    team.append(team_data)

                #print(team)

                player_data = {"team": team}

                game_data = {
                    "id": game_id,
                    "map": map,
                    "mode": mode,
                    "score": game_score,
                    "player_data": player_data
                }

                game.append(game_data)
            
            set_data = {
                "id": current_stage,
                "name": stage_round_names[i],
                "result": result,
                "score": set_score,
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

    data = {"bracket": bracket}
    individual_tournament = {
        "id": len(data['data']['tournaments']['individual_tournaments']) + 1,
        "name": series_name,
        "edition": edition,
        "date": date,
        "result": result,
        "data": data
    }
    
    data['data']['tournaments']['individual_tournaments'].append(individual_tournament)

    json_object = json.dumps(data, indent = 4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    
    print("Completed")
