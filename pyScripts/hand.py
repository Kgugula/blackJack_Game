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
    # Dict to store card values. B/c 'Card' object is a string
    
    def __init__(self):
        self.cards = []

    def get_value(self):

        values_list = []
        values = 0       

        
        for card in self.cards:
            values_list.append(Hand.CARD_VALUES[card[0]])

        # Ignore value add of aces until the optimal value determined; below
        
        for value in values_list:
                if value != "A":
                    values += value

        # While there is an ace in the hand - check values parameter to see what value of ace is optimal
        # Edge case if more than one ace in hand

        '''
        Enter while loop when hand has MULTIPLE aces.
        We know at most only one ace can hold the value of '11,'
        i.e. if two aces both held '11' hand.get_value() > 21.
        If current value of 'values' variable is less than '9'
        then we have room for one ace to hold an '11' and ALL subsequent aces
        must hold a '1.' Note that after adding value += 11 when the first ace is removed and take the value of '11',
        values variable will ALWAYS be greater than '9' and we will not enter first
        'if' statement below. Need to keep second 'if' statement in 'while' loop below
        in case there are 3 or 4 aces in hand. 

        '''

        while values_list.count("A") > 1:
            if values < 9:
                values_list.remove("A")
                values += 11
            else:
                values_list.remove("A")
                values += 1
            
        # While there is only one ace in hand; different conditions
        # Will not enter above 'while' loop

        if values_list.count("A") == 1:
        
            if values <=10:
                values_list.remove("A")
                values += 11
            else:
                values_list.remove("A")
                values += 1

        return values

        
    def add_to_hand(self, cards_dealt): # list of card objects

        for card in cards_dealt:
            self.cards.append(card)

    # Method to clear hand; for the start of new rounds
    
    def clear_hand(self):

        self.cards *= 0

    # Dunder methods
           
    def __str__(self):

        str_hand = ', '.join([str(x)for x in self.cards])
        return str_hand

    # Player script has identical function __str__. Necessary?

    def __len__(self):
        count = 0
        for card in self.cards:
            count += 1
        return count















