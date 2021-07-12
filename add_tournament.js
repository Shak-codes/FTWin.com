function add_tournament() {

    // Prompts user for tournament series name
    let series_name = window.prompt("What is the name of the tournament series?\n");

    // Prompts user for tournament edition
    let edition = window.prompt("What is the edition of the tournament series?\n");

    // Prompts user for tournament date
    let date = window.prompt("What was the date of the tournament\n");

    // Prompts user for tournament placing
    let result = window.prompt("What place did you get in the tournament?\n");

    // Prompts user for tournament stage data (IE. Swiss stage then Top Cut)
    let stages_length = parseInt(window.prompt("How many stages did the tournament have?\n"));
    let stages = [];

    // the number of sets per tournament stage (ie. swiss, ladder, bracket, ect) (NOT actual maps)
    let sets_per_stage = [];

    // title of the match in the tournament (ie. Winner's Finals, Loser's Semis, if swiss: Round 3)
    let stage_round_names = [];

    // the number of games played in each set
    let stage_games = [];

    for (let stage = 0; stage < stages_length; stage++) {

        // Prompts user for name of tournament stage. The "current_stage" is the incremented value of the stage to account for the "stages" array starting at index 0. The user's response
        // is then pushed onto the "stages", array.
        let current_stage = stage + 1;
        let name = window.prompt("What is the name of stage " + current_stage + " ?\n");
        stages.push(name);

        // Prompts user for the number of sets in the specific stage. Pushes the response as an integer onto the "sets_per_stage" array.
        let sets = parseInt(window.prompt("How many sets were in the " + stages[stage] + " stage?\n"));
        sets_per_stage.push(sets);

        // Initializes the index at 0
        let idx = 0;

        // Prompts user for the name of each set in the stage of the tournament.
        while (idx < sets_per_stage[stage]) {
            let prefix_count = window.prompt("How many rounds share the same prefix?(out of " + sets_per_stage[stage] - j + ")? \n");
            let prefix = window.prompt("What is the name of the prefix?\n");
            for (let i = 0; i < prefix_count; i++) {
                let round_name = prefix + " " + window.prompt("What round did you play?\n");
                stage_round_names.push(round_name);
                idx++;
            }
        }

        // Get number of games played for each set
        for (let i = 0; i < sets_per_stage[stage]; i++) {
            let game_count = window.prompt("How many games did you play in " + stage_round_names[i] + "?\n");
            stage_games.push(game_count);
        }

        for (let i = 0; i < sets_per_stage[stage]; i++) {
            let current_stage = i + 1
            let result = window.prompt("Set " + i + " result\n");
            let score = window.prompt("Set score\n");
            for (let j = 0; j < stage_games[i]; j++) {
                let map = window.prompt("Map name: ");
                let mode = window.prompt("Mode name: ");
                let score = window.prompt("Score: ");
                let team = [];
                for (let k = 0; k < 2; k++) {
                    team_id = k + 1;
                    team_name = window.prompt("Team name: ");
                    players = [];
                    weapons = [];
                    paint = [];
                    kills = [];
                    assists = [];
                    deaths = [];
                    for (let player = 0; player < 4; player++) {
                        player_name = window.prompt("Player " + player + " name: ");
                        players.push(player_name);
                        player_weapon = window.prompt("Player " + player + " weapon: ");
                        weapons.push(player_weapon);
                        player_paint = window.prompt("Player " + player + " paint: ");
                        paint.push(player_paint);
                        player_kills = window.prompt("Player " + player + " kills: ");
                        kills.push(player_kills);
                        player_assists = window.prompt("Player " + player + " assists: ");
                        assists.push(player_assists);
                        player_deaths = window.prompt("Player " + player + " deaths: ");
                        deaths.push(player_deaths);
                    }

                    let team = [];

                    
                }
            }
        } 


    }

}

// EDIT FUNCTION // VARIABLES RESET TO 0 AND OVERWRITE ARRAY ON TWO STAGE TOURNAMENTS