import random
from card import Card


class Deck:

    
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle() # shuffle deck upon instantiation

    def create_deck(self):
        for suit in Card.SUIT_SYMBOLS.values():
            for value in Card.VALUE_NAMES.values():
                newCard = str(Card(suit, value))
                self.cards.append(newCard)

        ''' Traverse through dictionaries in 'Card' class
            and initialize deck by creating new 'Card' object - I added a __len__ dunder method
            earlier to confirm that 52 elements added to list self.cards '''
                

    def shuffle(self):

        random.shuffle(self.cards) # shuffles deck in place

    def deal(self, num_cards):

        to_return_cards = []

        if num_cards > 1:
            cards_to_deal = self.cards[-num_cards:] # deal last 'n' cards out of shuffled deck
            for card in cards_to_deal:
                self.cards.remove(card)
                to_return_cards.append(card)
    
            return to_return_cards
        else:
            cards_to_deal = self.cards[-num_cards]
            to_return_cards.append(cards_to_deal)
            self.cards.remove(cards_to_deal)
            return to_return_cards



