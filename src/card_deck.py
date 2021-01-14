from operator import attrgetter
from src.card import Card

CARD_VALUE_STRINGS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
CARD_SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class CardDeck():   
    def __init__(self, shuffled=False):
        self.cards = []
        for suit in CARD_SUITS:
            for value in CARD_VALUE_STRINGS:
                self.cards.append((suit, value))

    def get_card_count(self):
        return len(self.cards)

    def pull_card_from_deck(self):
        return self.cards.pop()

    def sort_cards(self, sort_order = ['Spades', 'Hearts', 'Diamonds', 'Clubs']):
        sort_order_values = {key: i for i, key in enumerate(sort_order)}
        self.cards.sort(key=lambda x: sort_order_values[x[0]])

    def __repr__(self):
        card_count = self.get_card_count()
        if card_count == 1:
            plural = ''
        else:
            plural = 's'
        return f'Deck with {card_count} Card{plural}'

deck = CardDeck()
# deck.sort_cards(['Spades', 'Clubs', 'Diamonds', 'Hearts'])
# for card in deck.cards:
#     print(card)
card = deck.pull_card_from_deck()
print(card)
card = deck.pull_card_from_deck()
print(card)
card = deck.pull_card_from_deck()
print(card)
print(deck)
