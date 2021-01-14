import pytest
from src.card import Card

def test_card():
    card = Card(1, 'heart')
    assert type(card) == Card

def test_card_repr1():
    card = Card(1, 'heart')
    assert str(card) == 'Ace of Hearts'

def test_card_repr2():
    card = Card(2, 0)
    assert str(card) == '2 of Clubs'

def test_card_repr3():
    card = Card(12, 'spade')
    assert str(card) == 'Queen of Spades'
