from hand import Hand

class Player:

    '''
    Player objects will be instantiated upon instatiation of 'Game' object. Additionally,
    'Hand' object instantiated upon instatiation of 'Player' object.
    '''

    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def get_str_hand(self):
            str_hand = ", ".join([str(card) for card in self.hand.cards])
            return str_hand_combined

    

