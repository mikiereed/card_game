import pytest
from src.card_deck import CardDeck

def test_card_deck_init():
    card_deck = CardDeck()
    assert str(card_deck) == 'Deck with 52 Cards'

def test_pull_card_from_deck():
    card_deck = CardDeck()
    card = card_deck.pull_card_from_deck()
    is_right_type = isinstance(card, tuple)
    is_pulled_from_deck = (card_deck.get_card_count() == 51)
    assert is_right_type and is_pulled_from_deck

class TestSortCards():
    
    def test_sort_cards_default(self):
        card_deck = CardDeck()
        card_deck.sort_cards()
        sorted_suits = self.get_suits_from_sort(card_deck.cards)
        expected = ['Spades', 'Hearts', 'Diamonds', 'Clubs'] # default from CardDeck.sort_cards() method
        assert sorted_suits == expected

    def test_sort_cards(self):
        card_deck = CardDeck()
        card_deck.sort_cards(['Clubs', 'Hearts', 'Spades', 'Diamonds'])
        sorted_suits = self.get_suits_from_sort(card_deck.cards)
        expected = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        assert sorted_suits == expected

    def get_suits_from_sort(self, deck):
        """Return the suits for the 1st, 14th, 27th, 40th cards"""
        suits = [suit for suit, value in deck]
        suits = suits[0::13]
        return suits
