import pytest
from src.card import Card

def test_card():
    card = Card(1, 'heart')
    assert type(card) == Card

# class TestCardRepr():

#     def test_card_repr1(self):
#         card = Card(1, 'heart')
#         assert card == ('Hearts', 'Ace')

#     def test_card_repr2(self):
#         card = Card(2, 0)
#         assert str(card) == '2 of Clubs'

#     def test_card_repr3(self):
#         card = Card(12, 'spade')
#         assert str(card) == 'Queen of Spades'

# def test_card_suit():
#     card = Card(3, 'Hearts')
#     assert card.suit == 'heart'

# def test_card_value():
#     card = Card(5, 1)
#     assert card.value == 5
