# **************************************** #
#                                          #
#           ~~~ IMPORT MY CLASSES ~~       #
#                                          #
# **************************************** #

import sys
sys.path.insert(0, 'D:\PROGRAMMATION\PYTHON_PROJECTS\SoccerAnalytics_2017-2018_PremierLeague_BrightonReport\classes')

from WyscoutLeague import WyscoutLeague
from WyscoutTeam   import WyscoutTeam
# from classes.WyscoutPlayer import WyscoutPlayer


# **************************************** #
#                                          #
#           ~~~ IMPORT JSONs FILES ~~~     #
#                                          #
# **************************************** #

# import json

# wyscoutFolderPath = "../../wyscout_data/"

# with open(wyscoutFolderPath + "competitions.json") as competitionsFile:
#     competitions = json.load(competitionsFile)

# with open(wyscoutFolderPath + "teams.json") as teamsFile:
#     teams = json.load(teamsFile)

# with open(wyscoutFolderPath + "players.json") as playerFile:
#     players = json.load(playerFile)

# with open(wyscoutFolderPath + "matches/matches_England.json") as matchesFile:
#     matches = json.load(matchesFile)
    
# with open(wyscoutFolderPath + "events/events_England.json") as eventsFile:
#     events = json.load(eventsFile)
    
# **************************************** #
#                                          #
#           ~~~ INSTANTIATE LEAGUE ~~~     #
#                                          #
# **************************************** #

leagueCountry = "England"
leagueName    = "English first division"
season        = "2017"

premierLeague = WyscoutLeague(leagueCountry, leagueName, season)
print(premierLeague._teamNames)

# **************************************** #
#                                          #
#           ~~~ INSTANTIATE TEAM ~~~       #
#                                          #
# **************************************** #

teamName = "Brighton & Hove Albion"
brighton = WyscoutTeam(teamName)
print(brighton._playerNames)
