class WyscoutPlayer:
    '''
    This class defines a player from Wyscout database  
    '''
    
    # **************************************** #
    #                                          #
    #           ~~~ CONSTRUCTOR ~~~            #
    #                                          #
    # **************************************** #
    
    def __init__(
                    self,
                    id,
                    name,
                    age,
                    position,
                    matchPlayed,
                    matchPlayedIds
                ):
        
        print("Player created !")
        
        self._id             = id
        self._name           = name
        self._age            = age
        self._position       = position
        self._matchPlayed    = matchPlayed
        self._matchPlayedIds = matchPlayedIds
        
    # **************************************** #
    #                                          #
    #           ~~~ METHODS ~~~                #
    #                                          #
    # **************************************** #
        
    def getDefendingDuelSuccessRate():
        ...
    
    def getAirDuelSuccessRate():
        ...
    
    def getInterceptionPerGame():
        ...
    
    def getPlayerSmartPassSuccessRate():
        ...