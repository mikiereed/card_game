card_value_strings = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
card_suits = ['club', 'diamond', 'heart', 'spade']

class Card():
    suit = ''
    value = 0
    
    def __init__(self, value, suit):
        if isinstance(suit, str):
            self.suit = self.__str_to_suit(suit)
        else:
            self.suit = suit
        self.value = value

    def __value_to_str(self):
        return card_value_strings[self.value - 1] # for zero based list

    def __suit_to_str(self):
        return card_suits[self.suit]

    def __str_to_suit(self, suit_str):
        return card_suits.index(suit_str)

    def __repr__(self):
        return f'{self.__value_to_str().title()} of {self.__suit_to_str().title()}s'