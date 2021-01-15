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

@pytest.mark.parametrize('sort_order', [
    pytest.param(['Clubs', 'Hearts', 'Spades', 'Diamonds'], id='clubs, hearts, spades, diamonds'),
    pytest.param(['Hearts', 'Spades', 'Diamonds', 'Clubs'], id='hearts, spades, diamonds, clubs')])
def test_sort_cards(sort_order):
    card_deck = CardDeck(shuffled=True)
    card_deck.sort_cards(sort_order)
    sorted_cards_sample = card_deck.cards[::13]
    expected = [(sort_order[0], '2'), (sort_order[1], '2'), (sort_order[2], '2'), (sort_order[3], '2')]
    assert sorted_cards_sample == expected
