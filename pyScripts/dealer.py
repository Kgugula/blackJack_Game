from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def get_str_hand(self):
        str_hand = [str(card) for card in self.hand.cards]
        str_hand_combined = ", ".join(str_hand)
        return str_hand_combined
        

    def hit(self):
        if self.hand.get_value() <= 16:
            return True
