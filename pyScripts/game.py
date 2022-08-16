from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):

        # While loop to confirm if user (player) would like to "join" table
        while True:
            userInput = input(f"You are staring with ${self.player.balance}. Would you like to play a hand? ")
            if userInput.lower() == "yes":
                              break

        # While loop to prompt user to enter bet amount. Subject to contraints
        while True:
            userBet = int(input("Place your bet: " ))
            if userBet < Game.MINIMUM_BET:
                print("The minimum bet is $1")
        
            elif userBet > self.player.balance:
                print("You do not have sufficient funds.")

            else:
                self.bet = userBet
                break

            ''' At the start of the game need to
                deal two cards to both the dealer and player. Going
                to create a function to do this '''


        # Initialize Player & Dealer 'Hand' objects

        player_hand = Hand()
        dealer_hand = Hand()

        # Deal two cards per player
        # Going to use this as a 'counter' variable so I don't have to hardcode

        cards_to_deal = 2
        
        first_two_cards_player = self.deck.deal(cards_to_deal)
        player_hand.add_to_hand(first_two_cards_player)

        first_two_cards_dealer = self.deck.deal(cards_to_deal)
        dealer_hand.add_to_hand(first_two_cards_dealer)

        # Second dealer card must be displayed as 'Unknown' until his turn

        placeholder_dealer_card = dealer_hand.cards[1]
        #dealer_hand.cards.remove(dealer_hand.cards[1])
        dealer_hand.cards[1] = "Unkown" 
        

        # Display hands for player & dealer

        print(f"You are dealt: {str(player_hand)}")
        print(f"The dealer is dealt: {str(dealer_hand)}")
        
        
        # Decrement cards to deal
        # Now every time player/dealer 'hits' - just one card dealt

        cards_to_deal -= 1


                
            



            

