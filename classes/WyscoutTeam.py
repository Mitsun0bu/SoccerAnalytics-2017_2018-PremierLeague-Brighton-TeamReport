# **************************************** #
#                                          #
#           ~~~ LOAD DATA ~~~              #
#                                          #
# **************************************** #

import json

wyscoutFolderPath = "../../wyscout_data/"

with open(wyscoutFolderPath + "teams.json") as teamsFile:
    teams = json.load(teamsFile)

with open(wyscoutFolderPath + "players.json") as playerFile:
    players = json.load(playerFile)

class WyscoutTeam:
    '''
    This class defines a team from Wyscout database  
    '''

    # **************************************** #
    #                                          #
    #           ~~~ CONSTRUCTOR ~~~            #
    #                                          #
    # **************************************** #
    
    def __init__(self, name):
        
        self._name            = name
        self._id              = self.getId(teams, self._name)
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
        self.getPlayerInfos(players, self._id)
    
    # **************************************** #
    #                                          #
    #           ~~~ CLASS METHOD ~~~           #
    #                                          #
    # **************************************** #
    
    def getId(self, teams, teamName):
        '''
        Parameters :
            teams    : list
            teamName : string

        Returns    :
            The ID of a given team
        '''
        for team in teams:
            if team['name'] == teamName :
                return team['wyId']

    def getPlayerInfos(self, players, teamId):
        '''
        Parameters :
            players  : list
            teamId   : int

        Returns    :
            Update lists of player IDs / names for a given team,
            in function of their role
        '''        
        for player in players:
            if (player['currentTeamId'] == teamId):
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