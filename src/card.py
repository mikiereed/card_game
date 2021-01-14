card_value_strings = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
card_suits = ['club', 'diamond', 'heart', 'spade']

class Card():  
    def __init__(self, value, suit):
        if isinstance(suit, int):
            self.suit = self.__suit_to_str(suit)
        else:
            self.suit = self.__clean_suit_str(suit)
        self.value = value

    def __clean_suit_str(self, suit_str):
        clean_suit_str = suit_str.lower()
        if clean_suit_str[-1:] == 's':
            return clean_suit_str[:-1]
        else:
            return clean_suit_str

    def __value_to_str(self):
        return card_value_strings[self.value - 1] # for zero based list

    def __suit_to_str(self, suit_int):
        return card_suits[suit_int]

    def __str_to_suit(self, suit_str):
        return card_suits.index(suit_str)

    def __repr__(self):
        return (f'{self.suit.title()}s', {self.__value_to_str().title()})