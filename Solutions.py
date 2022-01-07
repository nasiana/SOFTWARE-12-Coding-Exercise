# ----------------------------------------

def determine_winner_general(games, results):

    teams = {}
    for i in range(len(games)):
        for team in games[i]:
            if team not in teams.keys():
                teams[team] = 0

    for i in range(0,len(games)):
        if results[i] == 0:
            # away team wins
            teams[games[i][1]] += 1
        else:
            # home team wins
            teams[games[i][0]] += 1


    top_score = 0
    for k,v in teams.items():
        if v > top_score:
            top_score = v
            winner = k
    return winner

# ----------------------------------------

def get_unique_teams(competitions):
    """Get list of unique teams for each list of competitions"""
    list_of_unique_teams = []
    for competition in competitions:
        for team in competition:
            if team in list_of_unique_teams:
                pass
            else:
                list_of_unique_teams.append(team)
    return list_of_unique_teams


class Team:
    """Create team objects"""
    def __init__(self, name, points=0):
        self.name = name
        self.points = 0

    def add_points(self):
        self.points += 3


def create_teams(list_of_teams):
    """Create team object for each unique team"""
    team_as_objects = []
    for item in list_of_teams:
        new_team = Team(item)
        team_as_objects.append(new_team)
    return team_as_objects


def winner(competitions, results):
    """Define winner based on given list of competitions and list of results provided"""
    winner = ""
    max_points = 0
    list_of_teams = get_unique_teams(competitions)
    teams = create_teams(list_of_teams)
    games = len(results)
    for n in range(games):
        if results[n] == 0:
            for team in teams:
                if competitions[n][1] == team.name:
                    team.add_points()
                else:
                    pass
        if results[n] == 1:
            for team in teams:
                if competitions[n][0] == team.name:
                    team.add_points()
                else:
                    pass
    print("Teams scores: ")
    for team in teams:
        print(team.name, team.points)
        if team.points > max_points:
            winner = team.name
    print("The winner is: "+winner)
    return(winner)

# ----------------------------------------

def get_teams(competitions):
    """Returns all teams as a dictionary, all teams with score of zero"""
    dict_of_teams = {}
    for competition in competitions:
        for team in competition:
            if team not in dict_of_teams.items():
                dict_of_teams[team] = 0
    return dict_of_teams


def get_score(competitions,results):
    """Attributes scores for each team taking into consideration array of results"""
    teams_as_a_dict = get_teams(competitions)
    for n in range(len(competitions)):
        if results[n] == 0:
            teams_as_a_dict[competitions[n][1]] += 3
        if results[n] == 1:
            teams_as_a_dict[competitions[n][0]] += 3
    print("All teams and scores: ")
    print(teams_as_a_dict)
    return(teams_as_a_dict)


def get_winner(dict):
    """Returns the winner, ie, the highest value on the dict of teams"""
    winner = ""
    highest_score = max(dict.values())
    print("Highest score: ", highest_score)
    for key, value in dict.items():
         if value == highest_score:
             winner = key
    print("The winner is: "+ winner)


get_winner(get_score(competitions_1,results_1))
get_winner(get_score(competitions_2,results_2))
get_winner(get_score(competitions_3,results_3))

# ----------------------------------------
def update_score(mydict,team,num):
    
    if team not in mydict.keys():
        mydict[team] = 0 #problem here cause I need to initialise it 
    mydict[team] += num
    return mydict

def func(competitions,results):
    if 

    dict_ = {}
    for i in range(len(competitions)):
        competing_teams = competitions[i] #the inner list eg ['Panthers', 'Lionesses']
        if results[i] == 1:
            dict_ = update_score(dict_,competing_teams[0],3) #adds 3 to the home team 
            dict_ = update_score(dict_,competing_teams[1],0) #add 0 to the away team
            
        else: 
            dict_ = update_score(dict_,competing_teams[1],3) #adds 3 to the away team 
            dict_ = update_score(dict_,competing_teams[0],0) #add 0 to the home team 
    
    for key,value in dict_.items():
        if value == max(dict_.values()):
            winner = key 
            return "winner is {}".format(winner)
    
            

print(func(competitions1,results1))
print(func(competitions2,results2))
print(func(competitions3,results3))

# ----------------------------------------

comp_res = list((competitions [i], results[i]) for i in range(len(results)))
list_winner = []
for i in comp_res:
    if i[1] == 1:
        winner = i[0][0]
    elif i[1] == 0:
        winner = i[0][1]
    list_winner.append(winner)


most_common = max(list_winner, key = list_winner.count)
print('The winner is {}'.format(most_common))

# ----------------------------------------

def winner(competitions, results):
    
    winners = {}

    for i, competition in enumerate(competitions):
        home = competition[0]
        away = competition[1]
        winners[home] = 0
        winners[away] = 0
        
    for i, competition in enumerate(competitions):
        home = competition[0]
        away = competition[1]
        if results[i] == 1:
            winners[home] += 3
        elif results[i] == 0:
            winners[away] += 3
            
    winner = max(winners, key=winners.get)

    return winner 

# ----------------------------------------

import numpy as np

def tournament_winner(matches, results):
    teams = np.unique(matches)

    winner_dict = {team: 0 for team in teams}

    for i in range(len(results)):
        if results[i] == 0:
            winner = matches[i][1] 
            current_score = winner_dict.get(winner)
            current_score +=3
            winner_dict[winner] = current_score

        else:
            winner = matches[i][0]
            current_score = winner_dict.get(winner)
            current_score +=3

            winner_dict[winner] = current_score

    print(winner_dict)
    val = list(winner_dict.values())
    val.sort()
    if val[-1]>val[-2]:
        fin_max = max(winner_dict, key=winner_dict.get)
        print('The winner is: ', fin_max)
    else:
        print('There is no clear winner')

    return winner_dict

