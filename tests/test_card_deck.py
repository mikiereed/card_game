import pytest
from src.card_deck import CardDeck

def test_card_deck_init():
    card_deck = CardDeck()
    assert str(card_deck) == 'Deck with 52 Cards'


class TestPullCard():

    def test_pull_card_removal_from_deck(self):
        card_deck = CardDeck()
        card_deck.pull_card_from_deck()
        assert card_deck.get_card_count() == 51

    def test_pull_card_return(self):
        card_deck = CardDeck()
        card = card_deck.pull_card_from_deck()
        assert isinstance(card, tuple)

    def test_pull_from_empty_deck(self):
        card_deck = CardDeck()
        while card_deck.cards:
            card_deck.pull_card_from_deck()
        with pytest.raises(IndexError):
            card_deck.pull_card_from_deck()

def test_shuffle_cards():
    card_deck = CardDeck(shuffled=False)
    unshuffled_cards_sample = card_deck.cards[:5]
    card_deck.shuffle_cards()
    shuffled_cards_sample = card_deck.cards[:5]
    assert unshuffled_cards_sample != shuffled_cards_sample


class TestSortCards():
    
    def test_sort_cards_default(self):
        card_deck = CardDeck(shuffled=True)
        card_deck.sort_cards()
        sorted_cards_sample = card_deck.cards[::13]
        # default suits order from CardDeck.sort_cards() method
        expected = [('Spades', '2'), ('Hearts', '2'), ('Diamonds', '2'), ('Clubs', '2')]
        assert sorted_cards_sample == expected

    def test_sort_cards(self):
        card_deck = CardDeck(shuffled=True)
        card_deck.sort_cards(['Clubs', 'Hearts', 'Spades', 'Diamonds'])
        sorted_cards_sample = card_deck.cards[::13]
        expected = [('Clubs', '2'), ('Hearts', '2'), ('Spades', '2'), ('Diamonds', '2')]
        assert sorted_cards_sample == expected
