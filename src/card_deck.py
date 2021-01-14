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

    def sort_cards(self, sort_order = ['Spades', 'Hearts', 'Diamonds', 'Clubs']):
        sort_order_values = {key: i for i, key in enumerate(sort_order)}
        print(sort_order_values)
        # self.deck.sort(key=attrgetter('suit', 'value'))
        # key=lambda x: sort_order_values[x['suit']]

    def __repr__(self):
        card_count = self.get_card_count()
        if card_count == 1:
            plural = ''
        else:
            plural = 's'
        return f'Deck with {card_count} Card{plural}'

deck = CardDeck()
# for card in deck.deck:
    # print(card)
deck.sort_cards(['Spades', 'Clubs', 'Diamonds', 'Hearts'])
print(deck)
