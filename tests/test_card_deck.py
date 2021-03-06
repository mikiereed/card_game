"""Tests for card_deck.py and the CardDeck() class.

This module contains all the tests for the card_deck.py file. It
has at least one test for every function in the CardDeck() class.

This package is called and run through pytest.
"""

import pytest
from src.card_deck import CardDeck

def test_card_deck_init():
    """Tests that the CardDeck() is properly initialized."""
    card_deck = CardDeck()
    assert str(card_deck) == 'Deck with 52 Cards'

def test_pull_card_removal_from_deck():
    """Tests that pull_card_from_deck() properly removes a card from the deck."""
    card_deck = CardDeck()
    card_deck.pull_card_from_deck()
    assert card_deck.get_card_count() == 51

def test_pull_card_return():
    """Tests that pull_card_from_deck() properly returns a card."""
    card_deck = CardDeck()
    card = card_deck.pull_card_from_deck()
    assert isinstance(card, tuple)

def test_pull_from_empty_deck():
    """Tests that pull_card_from_deck() properly raises an exception when deck is empty."""
    card_deck = CardDeck()
    while card_deck.cards:
        card_deck.pull_card_from_deck()
    with pytest.raises(IndexError):
        card_deck.pull_card_from_deck()

def test_shuffle_cards():
    """Tests that the shuffle_cards() works properly."""
    card_deck = CardDeck(shuffled=False)
    unshuffled_cards_sample = card_deck.cards[:5]
    card_deck.shuffle_cards()
    shuffled_cards_sample = card_deck.cards[:5]
    assert unshuffled_cards_sample != shuffled_cards_sample

@pytest.mark.parametrize('sort_order', [
    pytest.param(['Clubs', 'Hearts', 'Spades', 'Diamonds'], id='clubs, hearts, spades, diamonds'),
    pytest.param(['Hearts', 'Spades', 'Diamonds', 'Clubs'], id='hearts, spades, diamonds, clubs')])
def test_sort_cards(sort_order):
    """Tests that the sort_cards() sorts cards in the proper order."""
    card_deck = CardDeck(shuffled=True)
    card_deck.sort_cards(sort_order)
    sorted_cards_sample = card_deck.cards[::13]
    expected = [(sort_order[0], '2'),
                (sort_order[1], '2'),
                (sort_order[2], '2'),
                (sort_order[3], '2')]
    assert sorted_cards_sample == expected
