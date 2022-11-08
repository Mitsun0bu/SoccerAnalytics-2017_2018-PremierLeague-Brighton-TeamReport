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
#           ~~~ INSTANTIATE LEAGUE ~~~     #
#                                          #
# **************************************** #

leagueCountry = "England"
leagueName    = "English first division"
seasonYear    = "2017"

premierLeague = WyscoutLeague(leagueCountry, leagueName, seasonYear)

# **************************************** #
#                                          #
#           ~~~ INSTANTIATE TEAM ~~~       #
#                                          #
# **************************************** #

teamName = "Brighton & Hove Albion"
brighton = WyscoutTeam(teamName, seasonYear)

