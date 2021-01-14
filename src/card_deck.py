from operator import attrgetter
import random
from src.card import Card

CARD_VALUE_STRINGS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
CARD_SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class CardDeck():   
    def __init__(self, shuffled=False):
        self.cards = []
        for suit in CARD_SUITS:
            for value in CARD_VALUE_STRINGS:
                self.cards.append((suit, value))
        if shuffled == True:
            self.shuffle_cards()

    def get_card_count(self):
        return len(self.cards)

    def pull_card_from_deck(self):
        return self.cards.pop()

    def shuffle_cards(self):
        shuffled_cards = []
        while self.cards:
            random_number = random.randint(0, self.get_card_count() - 1)
            random_card = self.cards.pop(random_number)
            shuffled_cards.append(random_card)
        self.cards = shuffled_cards.copy()

    def sort_cards(self, sort_order = ['Spades', 'Hearts', 'Diamonds', 'Clubs']):
        sort_order_suits = {key: i for i, key in enumerate(sort_order)}
        sort_order_values = {key: i for i, key in enumerate(CARD_VALUE_STRINGS)}
        self.cards.sort(key=lambda x: (sort_order_suits[x[0]], sort_order_values[x[1]]))

    def __repr__(self):
        card_count = self.get_card_count()
        if card_count == 1:
            plural = ''
        else:
            plural = 's'
        return f'Deck with {card_count} Card{plural}'
        