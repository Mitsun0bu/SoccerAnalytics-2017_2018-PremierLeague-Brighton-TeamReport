class WyscoutTeam:
    '''
    This class defines a team from Wyscout database  
    '''

    # **************************************** #
    #                                          #
    #           ~~~ CONSTRUCTOR ~~~            #
    #                                          #
    # **************************************** #
    
    def __init__(self, id, name, playerIds, playerNames):
        
        print("Team created !")
        
        self._id             = id
        self._name           = name
        self._playerIds      = playerIds
        self._playerNames    = playerNames
    
    # **************************************** #
    #                                          #
    #           ~~~ METHODS ~~~                #
    #                                          #
    # **************************************** #
    
    def getGoalkeeprsIds():
        ...

    def getDefenderIds():
        ...
    
    def getMidfielderIds():
        ...
        
    def getStrikerIds():
        ...
    
    