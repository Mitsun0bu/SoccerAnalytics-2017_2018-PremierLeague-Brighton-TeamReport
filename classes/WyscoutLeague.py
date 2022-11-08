# **************************************** #
#                                          #
#           ~~~ LOAD DATA ~~~              #
#                                          #
# **************************************** #

import json

wyscoutFolderPath = "../../wyscout_data/"

with open(wyscoutFolderPath + "competitions.json") as competitionsFile:
    competitions = json.load(competitionsFile)

with open(wyscoutFolderPath + "teams.json") as teamsFile:
    teams = json.load(teamsFile)


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
        self._id        = self.getId(competitions, self._name)
        self._teamIds   = self.getTeamIds(teams, self._country)
        self._teamNames = self.getTeamNames(teams, self._country)

    # **************************************** #
    #                                          #
    #           ~~~ CLASS METHOD ~~~           #
    #                                          #
    # **************************************** #

    def getId(self, competitions, competitionName):
        '''
        Parameters :
            competitions   : list
            competitonName : string

        Returns    :
            The ID of a given competition
        '''
        for competition in competitions:
            if competition['name'] == competitionName :
                return competition['wyId']
    
    def getTeamIds(self, teams, country):
        '''
        Parameters :
            teams    : list
            country  : string

        Returns    :
            The ID of all teams from a given country
        '''
        teamIdList = []
        for team in teams:
            if team['area']['name'] == country and team['name'] != "England":
                teamIdList.append(team['wyId'])
        return teamIdList
    
    def getTeamNames(self, teams, country):
        '''
        Parameters :
            teams    : list
            country  : string

        Returns    :
            The names of all teams from a given country
        '''
        teamNameList = []
        for team in teams:
            if team['area']['name'] == country and team['name'] != "England":
                teamNameList.append(team['name'])
        return teamNameList
    