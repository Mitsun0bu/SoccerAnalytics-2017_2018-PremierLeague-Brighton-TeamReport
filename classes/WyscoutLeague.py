class WyscoutLeague:
    '''
    This class defines a league from Wyscout database  
    '''

    # **************************************** #
    #                                          #
    #           ~~~ CONSTRUCTOR ~~~            #
    #                                          #
    # **************************************** #
    
    def __init__(self, id, name, teamIds, teamNames):
        
        print("League created !")
        
        self._id        = id
        self._name      = name
        self._teamIds   = teamIds
        self._teamNames = teamNames