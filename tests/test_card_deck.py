import pytest
from src.card_deck import CardDeck

def test_card_deck_init():
    card_deck = CardDeck()
    assert str(card_deck) == 'Deck with 52 Cards'

# class TestSortCards():
    
#     def test_sort_cards_default():
