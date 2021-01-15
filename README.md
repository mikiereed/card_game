# card_game

#1, #2, & #3 below are accomplished through the CardDeck() class in the src/card_deck.py file.
#4 below is run in the src/game.py file.

1.	Shuffle cards in the deck: randomly mix the cards in the card deck, and return a whole deck of cards with a mixed order. 

2.	Get a card from the top of the deck: get one card from the top of the card deck, return a card, and if there is no card left in the deck, return error or exception.  

3.	Sort cards:  Sort cards in ascending order by suit and rank (ace high).
    i.e. If the deck contains cards with the following order:   
    (Spades, 2), (Diamonds, 5), (Spades, King), (Hearts, 3), (Clubs, Ace) 
    Sort cards ([Spades, Diamonds, Hearts, Clubs]) will return the cards with following order: 
    (Spades, 2), (Spades, King), (Diamonds, 5), (Hearts, 3), (Clubs, Ace)  

4.	Determine winners: 2 players play the game. They will draw 3 cards by taking turns. 
    -Whoever has the high score wins the game. 
    -Suit point number calculation: Clubs = 4, Hearts = 3, Diamonds = 2, Spades = 1
    -The winning value is calculated by suit point number * number in the card.
