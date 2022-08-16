class Dealer:
    def __init__(self):
        self.hand = []

    def get_str_hand(self):
        str_hand = [str(card) for card in self.hand]
        str_hand_combined = ", ".join(str_hand)
        return str_hand_combined
        

    def hit(self):
        pass
