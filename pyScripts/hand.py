class Hand:

    CARD_VALUES =  {"2": 2,         
                    "3": 3,
                    "4": 4,
                    "5": 5,
                    "6": 6,
                    "7": 7,
                    "8": 8,
                    "9": 9,
                    "T": 10,
                    "J": 10,
                    "Q": 10,
                    "K": 10,
                    "A": "A"
        
        }
    # Dict to store card values. B/c card object is a string
    
    def __init__(self):
        self.cards = []

    def get_value(self):

        values_list = []
        values = 0       

        
        for card in self.cards:
            values_list.append(Hand.CARD_VALUES[card[0]])

        for value in values_list:
                if value != "A":
                    values += value

        # While there is an ace in the hand - check values parameter to see what value of ace is optimal
        while values_list.count("A") >= 1:

            if values <= 10:
                values_list.remove("A")
                values += 11

            else:
                values_list.remove("A")
                values += 1

        return values

        
    def add_to_hand(self, cards_dealt): # list of card objects

        for card in cards_dealt:
            self.cards.append(card)


    def __str__(self):

        str_hand = ', '.join([str(x)for x in self.cards])
        return str_hand

        # player script has identical function. Necessary?
