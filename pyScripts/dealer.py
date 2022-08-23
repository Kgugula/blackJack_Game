from hand import Hand

class Dealer:
    
    def __init__(self):
        self.hand = Hand()

    '''
    Just like the Player class, Dealer class had 'Hand' object instantiated
    upon it's instantiation. This comes in useful for dealer class,
    because Dealer needs to know value of their hand in order to determine
    whether to hit or stay
    '''

    def get_str_hand(self):
        str_hand_combined = ", ".join([str(card) for card in self.hand.cards])
        return str_hand_combined
        

    def hit(self):
        if self.hand.get_value() <= 16:
            return True

    '''
    Only need to return a Boolean for 'hit' function..it's used for a 'while'
    loop in 'Game' class
    '''
