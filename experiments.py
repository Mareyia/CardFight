def death_check()
	death_check_2, empty_hand_check_2 = all_player[every_player][0].check_status()
	if death_check_2:
		print(all_player[every_player][0], "died!")
		#remove the player
		if all_player[every_player][1].position:
			A_map.remove_entity(all_player[every_player][1])
			number_of_alive_player -= 1

def condition_for_endgame(teams_given, game_mode_given, new_death=None):
	if new_death is not None:
		teams_given[new_death.team].remove(new_death)
	alive_teams = []
	for team in teams_given:
		for team_player in teams_given[team]:
			if team_player[1].position is not None:
				alive_teams.append(team)
				break
	return alive_teams


def end_game_message(teams_given, game_mode_given):
	if game_mode_given == "Campaing":
		for team in teams_given:
			if team == 1:
				return "\n{} defeated all oponments and WON THE GAME!!!\nCongratsulations!\n".format(teams_given[team][0][0].player_name)
			else:
				return "\nComputers destroyed you\nGAME OVER!!!\n"

1, 2, 3, 4, 5, 6

[]
[]
[]
[1, 2, 3]


def team_balance_check(given_answer, all_the_teams, number_of_player, all_the_players, mode_of_the_custom_game="Something else"):
	players_left = len(all_the_players.keys()) - number_of_player + 1
	empty_teams = {}
	for team in all_the_teams:
		if len(all_the_teams[team]) == 0:
			empty_teams[team] = all_the_teams[team]
	if empty_teams == players_left:
		print("Can't do, some teams will be left empty")
		to_continue(1)
		print("Autofilling")
		to_continue(1)
		if mode_of_the_custom_game == "Players vs Computers":
			if all_the_teams[1] == empty_teams[1]:
				return "n"
			else:
				return "y"
		else:
			return empty_teams.keys()[randint(range(0, len(empty_teams.keys())- 1))]
	return given_answer
