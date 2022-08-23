from deck import Deck
from hand import Hand
from player import Player

class Game:
    
    # Class attributues
    
    MINIMUM_BET = 1
    ROUND = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        self.exit_program = False

        # Function ends game - creates new Game object with self.player and self.dealer passed to it
        # If arguments not passed then we don't want to start another game - final print statement is below
    
    def end_game(player, dealer):
        
        try:
            new_game = Game(player, dealer)
            return new_game.start_game()
        
        except TypeError:
            print("The program has ended.")

    def start_game(self):

        # While loop to confirm if user (player) would like to "join" table
        
        while True:

        # If player balance is '0' - end program
        
            if self.player.balance == 0:
                print("-------------------")
                print("You lost all of your money. Exiting program...")
                self.exit_program = True
                Game.end_game()

        # If not the first round; use class method clear_hand() on Hand objects
        # Note that ROUND is an attribute of the 'Game' class
        
            if Game.ROUND != 1:
                self.player.hand.clear_hand()
                self.dealer.hand.clear_hand()

        # Accept user input

            userInput = input(f"You are staring with ${self.player.balance}. Would you like to play a hand? ")

            if userInput.lower() == "yes":
                              break
            elif userInput.lower() == "no":
                self.exit_program = True
                print("Exit Program.")
                Game.end_game()

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
            

        # Okay now we begin...

        '''
            Watch out for the instance attributes and the functions called from them.
            Many classes instantiate other classes upon their instantiation
            E.g. Player & Dealer both instantiate a Hand object from their respective
            __init__ methods. See respective scripts for more information

        '''
            
        cards_to_deal = 2

        # Connected to above comment
        # 'Player' object is an attribute of 'Game' class. Likewise, 'Hand' object is an attribute of 'Player' class

        self.player.hand.add_to_hand(self.deck.deal(cards_to_deal))
        self.dealer.hand.add_to_hand(self.deck.deal(cards_to_deal))

        # Need a mystery/placeholder card for the dealer

        dealer_placeholder = self.dealer.hand.cards[1]
        self.dealer.hand.cards[1] = "Unknown"

        print(f"You are dealt: {self.player.hand}")
        print(f"The dealer is dealt: {self.dealer.hand}")

        # Decrement counter variable

        cards_to_deal -= 1

        # Variable for edge case; player has a natural blackjack; intialize to 'False'

        player_natural_blackjack = False

        # While loop for player turn

        while True:

        # Edge case for if its a natural blackjack
        # Want to exit turn - no prompt for hit or stay
            
            if self.player.hand.get_value() == 21 and len(self.player.hand) == 2:
                player_natural_blackjack = True
                break
            
            playerTurn = input("Would you like to hit or stay? ")
            if playerTurn.lower() == "hit":

                self.player.hand.add_to_hand(self.deck.deal(cards_to_deal))
                print(f"You are dealt: {self.player.hand.cards[-1]}") 
                print(f"You now have: {self.player.hand}")
            

        # Each time the player hits - want to check the updated value of the hand

                if self.player.hand.get_value() > 21:
                    print(f"Your hand value is over 21 and you lose ${self.bet} :(")
                    self.player.balance -= self.bet
                    Game.ROUND += 1
                    return Game.end_game(self.player, self.dealer)

            elif playerTurn.lower() == "stay":
                break
            

            else:
                print("That is not a valid option.")

        # Dealer turn begins
        # First have to replace placeholder "Unknown" with actual card dealt

        self.dealer.hand.cards[1] = dealer_placeholder
        print(f"The dealer has: {self.dealer.hand}")

        # Edge case when player has blackjack
         
        while player_natural_blackjack:
            if self.dealer.hand.get_value() == 21:
                print("Two natural blackjacks!! You win $50,000")
                self.player.balance += 50000
                Game.ROUND += 1
                return Game.end_game(self.player, self.dealer)

        # If player has blackjack and dealer does not - end round. No option for dealer to hit or stay
        
            else:
                print(f"Blackjack! You win ${round((1.5 * self.bet))}.")
                self.player.balance += round((1.5 * self.bet))
                Game.ROUND += 1
                return Game.end_game(self.player, self.dealer)

        # If the dealer has a blackjack and the player does not; player loses

        if self.dealer.hand.get_value() == 21:
            print(f"Dealer has blackjack! You lose ${self.bet}.")
            self.player.balance -= self.bet
            Game.ROUND += 1
            return Game.end_game(self.player, self.dealer)

        
        # Check to see if dealer 'needs' to hit

        while self.dealer.hit():

            self.dealer.hand.add_to_hand(self.deck.deal(cards_to_deal))
            print(f"The dealer hits and is dealt: {self.dealer.hand.cards[-1]}")
            print(f"The dealer has: {self.dealer.hand}")
            # If dealer busts off this hit, game is over. Double the bet amount and assign to player balance
            if self.dealer.hand.get_value() > 21:
                print(f"The dealer busts, you win ${self.bet} :)")
                self.player.balance += self.bet
                Game.ROUND += 1
                return Game.end_game(self.player, self.dealer)


        
        
        # If the value of dealer cards >= 17; they must stay
        
        print("The dealer stays.")

        # If neither player or dealer busts during their turn; need to compare value of the hands

        if self.player.hand.get_value() > self.dealer.hand.get_value():
            print(f"You win ${self.bet}")
            self.player.balance += self.bet
        elif self.player.hand.get_value() == self.dealer.hand.get_value():
            print(f"Tie game! Bet is returned.")
            Game.ROUND += 1
            return Game.end_game(self.player, self.dealer)
        else:
            print(f"The dealer wins, you lose ${self.bet} :(")
            self.player.balance -= self.bet

        # Increment round
        
        Game.ROUND += 1

        return Game.end_game(self.player, self.dealer)

            


       
