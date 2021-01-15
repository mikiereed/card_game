"""A standard card deck with shuffling, sorting, and dealing features.

This module contains the CardDeck() class. It is made to represent a standard deck
of cards (4 suits, 13 cards per suit).The pull_card_from_deck() function returns the
final card from the deck, as if the cards were upside down and the top card was chosen.

  Typical usage example:

  card_deck = CardDeck(shuffled=false)
  card_deck.shuffle_cards()
  card_deck.sort_cards(sort_order = ['Clubs', 'Diamonds', 'Hearts', 'Spades'])
  card_count = card_deck.get_card_count() # 52
  top_card = card_deck.pull_card_from_deck()
  card_count = card_deck.get_card_count() # 51
"""

import random

CARD_VALUE_STRINGS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
CARD_SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class CardDeck():
    """Standard deck of cards and functions.

    Class represents a standard deck of cards (4 suits, 13 values per suit).
    User can initialize a CardDeck() either shuffled or unshuffled (default=unshuffled).

    Attributes:
        cards: An ordered list of the current cards in the deck.
    """
    def __init__(self, shuffled=False):
        """Inits CardDeck object with a deck of cards."""
        self.cards = []
        for suit in CARD_SUITS:
            for value in CARD_VALUE_STRINGS:
                self.cards.append((suit, value))
        if shuffled:
            self.shuffle_cards()

    def get_card_count(self):
        """Return the amount of cards left in the deck."""
        return len(self.cards)

    def pull_card_from_deck(self):
        """Remove and return the top card from the deck."""
        try:
            return self.cards.pop()
        except IndexError as deck_empty:
            raise IndexError("The deck is empty") from deck_empty

    def shuffle_cards(self):
        """Shuffle deck of cards using the random package."""
        shuffled_cards = []
        while self.cards:
            random_number = random.randint(0, self.get_card_count() - 1)
            random_card = self.cards.pop(random_number)
            shuffled_cards.append(random_card)
        self.cards = shuffled_cards.copy()

    def sort_cards(self, sort_order=None):
        """Sort cards based on suits (default or given), then by value (Ace high)."""
        sort_order_suits = {key: i for i, key in enumerate(sort_order)}
        sort_order_values = {key: i for i, key in enumerate(CARD_VALUE_STRINGS)}
        self.cards.sort(key=lambda x: (sort_order_suits[x[0]], sort_order_values[x[1]]))

    def __repr__(self):
        """CardDeck object is shown as 'Deck with n Cards'."""
        card_count = self.get_card_count()
        if card_count == 1:
            plural = ''
        else:
            plural = 's'
        return f'Deck with {card_count} Card{plural}'
