from card import Card

SUITS_COUNT = 4
VALUES_COUNT = 13

class CardDeck():
    deck = []
    
    def __init__(self, shuffled=False):
        suits = [x for x in range(SUITS_COUNT)]
        values = [x + 1 for x in range(VALUES_COUNT)]
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))
                print(Card(value, suit))

    def __repr__(self):
        return ','.join(self.deck)

deck = CardDeck()
print(deck)
