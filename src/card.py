card_value_strings = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Card():
    suit = ''
    value = 0
    
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __value_to_str(self):
        return card_value_strings[self.value - 1] # for zero based list

    def __repr__(self):
        return f'{self.__value_to_str()} of {self.suit}s'

card = Card(1, 'heart')
print(card)