from hand import Hand

class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def get_str_hand(self):
            str_hand = [str(card) for card in self.hand.cards]
            str_hand_combined = ", ".join(str_hand)
            return str_hand_combined

        # This seems a bit verbose. Going to circle back...
        # self.hand attribute only used to display 'string of hand'
        # Hand object will cover condition/functionality

