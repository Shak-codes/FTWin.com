function add_tournament() {

    // Get tournament series name
    let series_name = prompt("What is the name of the tournament series?\n");

    // Get tournament edition
    let edition = prompt("What is the edition of the tournament series?\n");

    // Get tournament date
    let date = prompt("What was the date of the tournament\n");

    // Get tournament placing
    let result = prompt("What place did you get in the tournament?\n");

    // Get tournament stage data (IE. Swiss stage then Top Cut)
    let stages_length = parseInt(prompt("How many stages did the tournament have?\n"));
    let stages = [];

    // number of sets per tournament stage
    let sets_per_stage = [];

    // name of each set in the tournament
    let stage_round_names = [];

    // number of games played for each set
    let stage_games = [];

    for (let stage = 0; stage < stages_length; stage++) {

        // Get name of tournament stage
        let current_stage = stage + 1;
        let name = prompt("What is the name of stage " + current_stage + " ?\n");
        stages.push(name);

        let sets = parseInt(prompt("How many sets were in the " + stages[stage] + " stage?\n"));
        sets_per_stage.push(sets);

        let idx = 0;

        // Get name of each set in the stage of the tournament
        while (idx < sets_per_stage[stage]) {
            let prefix_count = prompt("How many rounds share the same prefix?(out of " + sets_per_stage[stage] - j + ")? \n");
            let prefix = prompt("What is the name of the prefix?\n");
            for (let i = 0; i < prefix_count; i++) {
                let round_name = prefix + " " + prompt("What round did you play?\n");
                stage_round_names.push(round_name);
                idx++;
            }
        }

        // Get number of games played for each set
        for (let i = 0; i < sets_per_stage[stage]; i++) {
            let game_count = prompt("How many games did you play in " + stage_round_names[i] + "?\n");
            stage_games.push(game_count);
        }

        for (let i = 0; i < sets_per_stage[stage]; i++) {
            let current_stage = i + 1
            let result = prompt("Set " + i + " result\n");
            let score = prompt("Set score\n");
            for (let j = 0; j < stage_games[i]; j++) {
                let map = prompt("Map name: ");
                let mode = prompt("Mode name: ");
                let score = prompt("Score: ");
                let team = [];
                for (let k = 0; k < 2; k++) {
                    team_id = k + 1;
                    team_name = prompt("Team name: ");
                    players = [];
                    weapons = [];
                    paint = [];
                    kills = [];
                    assists = [];
                    deaths = [];
                    for (let player = 0; player < 4; player++) {
                        player_name = prompt("Player " + player + " name: ");
                        players.push(player_name);
                        player_weapon = prompt("Player " + player + " weapon: ");
                        weapons.push(player_weapon);
                        player_paint = prompt("Player " + player + " paint: ");
                        paint.push(player_paint);
                        player_kills = prompt("Player " + player + " kills: ");
                        kills.push(player_kills);
                        player_assists = prompt("Player " + player + " assists: ");
                        assists.push(player_assists);
                        player_deaths = prompt("Player " + player + " deaths: ");
                        deaths.push(player_deaths);
                    }

                    let team_data = {
                        id: team_id,
                        name: team_name,
                        players: players,
                        weapons: weapons,
                        paint: paint,
                        kills: kills,
                        assists: assists,
                        deaths: deaths
                    }
                    console.log(team_data);
                    team.push(team_data);

                }
                console.log(team);
            }
        } 


    }

}

add_tournament();

// EDIT FUNCTION // VARIABLES RESET TO 0 AND OVERWRITE ARRAY ON TWO STAGE TOURNAMENTS