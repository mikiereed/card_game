from operator import attrgetter
from src.card import Card

SUITS_COUNT = 4
VALUES_COUNT = 13

class CardDeck():   
    def __init__(self, shuffled=False):
        self.deck = []
        suits = [x for x in range(SUITS_COUNT)]
        values = [x + 1 for x in range(VALUES_COUNT)]
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))

    def get_card_count(self):
        return len(self.deck)

    def sort_cards(self, sort_order = ['spade', 'heart', 'diamond', 'club']):
        sort_order = self.__clean_suit_list(sort_order)
        sort_order_values = {key: i for i, key in enumerate(sort_order)}
        print(sort_order_values)
        # self.deck.sort(key=attrgetter('suit', 'value'))
        key=lambda x: sort_order_values[x['suit']]

    def __clean_suit_list(self, suit_list):
        clean_suit_list = []
        for suit in suit_list:
            suit = suit.lower()
            if suit[-1:] == 's':
                suit = suit[:-1]
            clean_suit_list.append(suit)
        
        return clean_suit_list

    def __repr__(self):
        card_count = self.get_card_count()
        if card_count == 1:
            plural = ''
        else:
            plural = 's'
        return f'Deck with {card_count} Card{plural}'

deck = CardDeck()
deck.sort_cards(['Spades', 'Club', 'diamonds', 'heart'])
print(deck)
