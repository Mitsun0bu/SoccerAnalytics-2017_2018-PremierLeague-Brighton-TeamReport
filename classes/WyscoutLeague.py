# **************************************** #
#                                          #
#           ~~~ IMPORT ~~~                 #
#                                          #
# **************************************** #

from statistics import mean

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
#           ~~~ DEFINE CLASS ~~~           #
#                                          #
# **************************************** #

class WyscoutLeague:
    '''
    This class defines a league from Wyscout database  
    '''

    # **************************************** #
    #                                          #
    #           ~~~ CONSTRUCTOR ~~~            #
    #                                          #
    # **************************************** #

    def __init__(self, country, name, season):

        self._country   = country

        self._name      = name

        self._season    = season

        self._id        = 0 
 
        self._teamIds   = []
        self._teamNames = []
        self.setTeamsInfo(teams)
        
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
        

        # DEFENDERS-RELATED VARIABLE
        self.defInterceptPerGame     = 0
        self.defGroundDuelWinRate    = 0
        self.defSmartPassSuccessRate = 0
        self.setDefenderRelatedVariables(events)
        
        
    # **************************************** #
    #                                          #
    #           ~~~ CLASS METHOD ~~~           #
    #                                          #
    # **************************************** #

    def setId(self, leagues):
        '''
        Parameters :
            leagues : list

        Action    :
            Set the ID of a league
        '''
        for league in leagues:
            if league['name'] == self._name :
                self._id = league['wyId']
    
    def setTeamsInfo(self, teams):
        '''
        Parameters :
            teams    : list

        Action     :
            Set the IDs / Names of all teams playing in a league
        '''

        for team in teams:
            if team['area']['name'] == self._country and team['name'] != self._country:
                self._teamIds.append(team['wyId'])
                self._teamNames.append(team['name'])
    
    def setPlayersInfo(self, players):
        '''
        Parameters :
            players  : list

        Action     :
            Set the different lists of player IDs / names,
            in function of their role
        '''        
        for player in players:
            if player['currentTeamId'] in self._teamIds:
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

    def setDefenderRelatedVariables(self, events):
        
        interceptTag               = 1401
        wonTag                     = 703
        accurateTag                = 1801

        interceptPerGameList       = []
        groundDuelWinRateList      = []
        smartPassSuccessRateList   = []

        for defenderId in self._defenderIds:
            
            gamesPlayedList        = []

            interceptCount         = 0

            groundDuelCount        = 0
            wonGroundDuelCount     = 0

            smartPassCount         = 0
            accurateSmartPassCount = 0
            
            for event in events:
                if event['playerId'] == defenderId:
                    # CREATE A LIST OF GAMES PLAYED
                    if event['matchId'] not in gamesPlayedList: 
                        gamesPlayedList.append(event['matchId'])
                    # COUNT THE NUMBER OF INTERCEPTIONS
                    for tag in event['tags']:
                        if tag['id'] == interceptTag:
                            interceptCount = interceptCount + 1
                    # COUNT THE NUMBER OF GROUND DEFENDING DUEL
                    if event['subEventName'] == "Ground defending duel":
                        groundDuelCount = groundDuelCount + 1
                        # COUNT THE NUMBER OF WON GROUND DEFENDING DUEL
                        for tag in event['tags']:
                            if tag['id'] == wonTag:
                                wonGroundDuelCount = wonGroundDuelCount + 1
                    # COUNT THE NUMBER OF SMART PASSES
                    elif event['subEventName'] == "Smart pass":
                         smartPassCount = smartPassCount  + 1
                         # COUNT THE NUMBER OF SUCCESSFUL SMART PASSES
                         for tag in event['tags']:
                             if tag['id'] == accurateTag:
                                 accurateSmartPassCount = accurateSmartPassCount + 1
            
            if len(gamesPlayedList):
                # ADD INTERCEPT PER GAME VALUE TO A LIST
                interceptPerGame = round((interceptCount / len(gamesPlayedList)), 1)
                interceptPerGameList.append(interceptPerGame)    
                
                # ADD GROUND DUEL SUCCESS RATE VALUE TO A LIST
                if groundDuelCount > 0:
                    groundDuelSuccessRate = round(((wonGroundDuelCount / groundDuelCount)  * 100), 1)
                else:
                    groundDuelSuccessRate = 0
                groundDuelWinRateList.append(groundDuelSuccessRate)
                
                # ADD SMART PASS SUCCESS RATE VALUE TO A LIST
                if smartPassCount > 0:
                    smartPassSuccessRate = round(((accurateSmartPassCount / smartPassCount)  * 100), 1)
                else:
                    smartPassSuccessRate = 0
                smartPassSuccessRateList.append(smartPassSuccessRate)

            self.defInterceptPerGame     = round(mean(interceptPerGameList), 1)
            self.defGroundDuelWinRate    = round(mean(groundDuelWinRateList), 1)
            self.defSmartPassSuccessRate = round(mean(smartPassSuccessRateList), 1)
    
    