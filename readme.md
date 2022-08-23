# BlackJack Game

The next of the ProgrammingExpert.io projects...implementing the card game blackjack using Python! I'm excited for this project, no doubt it will be a challenge but I think it will give me a great opportunity to practice with some OOP concepts as well as implementing longer/more complex programs in general.

I will try and add to this readme as I progress throughout the project. Here we go!

## Day 2 ##

I'm moving along on this project, my last commit was pushing starter code. To be candid I'm finding this fairly difficult - mainly because of all the classes/scripts involved. This is my first time working with multiple scripts. I can see how it should help with code readability and debugging...but for now it's just causing a bit of a headache. I'm only using one 10.5' display - yikes. 

I think it will help to redo a mindmap I created when yesterday when setting out on this project. I'm getting stuck on the granular stuff i.e. create a while loop to prompt user to do this, test out, debug, repeat. While what I think is a much better use of time is to connect all the classes and implement standalone code blocks at a time. 

Mutability is also a question that keeps popping into my head. With the use of mainly lists, it's getting touger to make sure my newly formed lists aren't effecting the old. I'm going to circle back and see where I can put some tuples, or maybe sets since the 'order' of a hand isn't an issue.

And now the real fun begins...implementing the logic behind the game, when does the dealer hit, how to get the value of a hand, what value will an ACE be in a given hand!?! Right now if you ran the main.py script you would make it to the point in the game where you and the dealer are both dealt two cards, and those cards are displayed on the user interface, with the second dealer card being displayed as 'Unknown'. 

## Day 5 ##

Passed a major hurdle yesterday. I was having trouble with tracking values between different classes (b/w Deck, Hand, Player, Dealer) classes. Specifically, I had Hand() objects which were not tracked to a specific instance of the Player or Dealer classes. This made the program feel very verbose and chunky, as I was constantly creating new variables to hold values in place, and to manually pass to the other objects that required them. This was giving me a headache and I was the one who wrote the code. The solution I found was instantiating a Hand() object upon instatiation of a Player object. So I could use all of the Hand() methods and attributes directly on the instance because it was located nicely inside the  'self.player object' or 'self.dealer' attribute of the Game() class, which were in themselves Player() and Dealer() objects themselves. Need a win and I got it. Making a mental note here that if your code 'feels' like it is ugly and doing too many unneccessary things...it probably is.

With that being said the bulk of work is now done on the project. Only a few things left to do like handle the edge case when the player is dealt a natural blackjack. I also need to implement some code (maybe a function within the Game() class) to end the game, or simply move on to the next round and start again when it is necessary. Right now the player could hit on their turn, bust, and the program would still go on to the dealer's turn. 

## Day 7 ## 

Finished the program!

It took awhile to debug - but it was fun. I might have played 50 hands or so and just had to make sure classes/functions where doing what they were meant to. Odd enough, for the case of the 'natural blackjack' it took some time to properly implement, I was getting a lot of small errors. 

New additions to improve use:
    - Game attribute called 'exit_program' which ends the program if the user enters 'no' to the first prompt
    - New static method in 'Game' class - end_game(player, dealer). Takes in two argument; self.player, and self.dealer from previous game. This way the player balance is carried forward. 

Further additions:
    - In the coming days I'm going to work through the code and see if I can shorten it if possible. Also going to add additional comments to explain the flow of the program. 

## Final Comments ##

I decided to go over the code and clean it up and add comments where necessary. I ended up removing some redundent blocks that were not doing anything - e.g 'Game' attribute 'exit_program' didn't actually do anything, just was switched to 'True' before the program ended. Did not need it. Also, went back and forth and adding & deleting the @staticmethod decorator above the end_game() function. It doesn't 'need' it, but I think it is good for whoever might open the code to know, hey, I don't want this method access to 'self.' Please someone send me an email if I am way wrong on that. 


On to the next project!

