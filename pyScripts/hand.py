class Hand:
    def __init__(self):
        self.cards = []

    def get_value(self):
        pass
        
    def add_to_hand(self, cards_dealt): # list of card objects

        if len(cards_dealt) > 1:
            for card in cards_dealt:
                self.cards.append(card)
        else:
            self.cards.append(cards_dealt)



    def __str__(self):

        str_hand = [str(card) for card in self.cards]
        str_hand_combined = ", ".join(str_hand)
        return str_hand_combined

        # player script has identical function. Necessary?


