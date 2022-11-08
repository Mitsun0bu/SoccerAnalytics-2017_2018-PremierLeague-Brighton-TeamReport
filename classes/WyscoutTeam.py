# **************************************** #
#                                          #
#           ~~~ LOAD DATA ~~~              #
#                                          #
# **************************************** #

import json

wyscoutFolderPath = "../../wyscout_data/"

with open(wyscoutFolderPath + "competitions.json") as competitionsFile:
    leagues = json.load(competitionsFile)

with open(wyscoutFolderPath + "teams.json") as teamsFile:
    teams = json.load(teamsFile)

with open(wyscoutFolderPath + "players.json") as playerFile:
    players = json.load(playerFile)

with open(wyscoutFolderPath + "matches/matches_England.json") as matchesFile:
    matches = json.load(matchesFile)
    
with open(wyscoutFolderPath + "events/events_England.json") as eventsFile:
    events = json.load(eventsFile)


# **************************************** #
#                                          #
#           ~~~ CLASS DEFINITION ~~~       #
#                                          #
# **************************************** #

class WyscoutTeam:
    '''
    This class defines a team from Wyscout database  
    '''

    # **************************************** #
    #                                          #
    #           ~~~ CONSTRUCTOR ~~~            #
    #                                          #
    # **************************************** #
    
    def __init__(self, name, seasonYear):
        
        self._name            = name

        self._id              = 0
        self.setId(teams)
    
        self._playerIds       = []
        self._goalkeeperIds   = []
        self._defenderIds     = []
        self._midfielderIds   = []
        self._forwardIds      = []
        self._playerNames     = []
        self._goalkeeperNames = []
        self._defenderNames   = []
        self._midfielderNames = []
        self._forwardNames    = [] 
        self.setPlayersInfo(players)

        self._matchIds        = []
        self.setSeasonMatchIds(matches, seasonYear)

        self._numMatchPlayed  = len(self._matchIds)
        
    
    # **************************************** #
    #                                          #
    #           ~~~ CLASS METHOD ~~~           #
    #                                          #
    # **************************************** #
    
    def setId(self, teams):
        '''
        Parameters :
            teams    : list

        Action     :
            Set the ID of a given team
        '''
        for team in teams:
            if team['name'] == self._name:
                self._id = team['wyId']

    def setPlayersInfo(self, players):
        '''
        Parameters :
            players  : list

        Action     :
            Set the different lists of player IDs / names,
            in function of their role
        '''        
        for player in players:
            if (player['currentTeamId'] == self._id):
                self._playerIds.append(player['wyId'])
                self._playerNames.append(player['shortName'])
                if player['role']['name'] == 'Goalkeeper':
                    self._goalkeeperIds.append(player['wyId'])
                    self._goalkeeperNames.append(player['shortName'])
                elif player['role']['name'] == 'Defender':
                    self._defenderIds.append(player['wyId'])
                    self._defenderNames.append(player['shortName'])
                elif player['role']['name'] == 'Midfielder':
                    self._midfielderIds.append(player['wyId'])
                    self._midfielderNames.append(player['shortName'])
                elif player['role']['name'] == 'Forward':
                    self._forwardIds.append(player['wyId'])
                    self._forwardNames.append(player['shortName'])
        
    def setSeasonMatchIds(self, matches, seasonYear):
        '''
        Parameters :
            matches    : list
            seasonYear : string

        Returns    :
            Set the list of match played by a team during a given season
        '''
        seasonId = 0
        for match in matches:
            if match['dateutc'].startswith(seasonYear + "-10"):
                seasonId = match['seasonId']
                break
            
        for match in matches:
            if match['seasonId'] == seasonId:
                teamsData = list(match['teamsData'].keys())
                if int(teamsData[0]) == self._id or int(teamsData[1]) == self._id:
                    self._matchIds.append(match['wyId'])
        