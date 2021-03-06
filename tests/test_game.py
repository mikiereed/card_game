"""Tests for card_deck.py and the CardDeck() class.

This module contains all the tests for the card_deck.py file. It
has at least one test for every function in the CardDeck() class.

This package is called and run through pytest.
"""

from src.card_deck import CardDeck
import src.game as game

def test_deal_and_print_cards_amount_of_cards():
    """Tests that _deal_and_print_cards() gives each player the right amount of cards."""
    card_deck = CardDeck()
    _, players_cards = game._setup_players_and_card_lists()
    game._deal_and_print_cards(card_deck, players_cards, column_width=0)

    cards_per_player = len(players_cards[0])
    expected_cards_per_player = game.CARDS

    assert cards_per_player == expected_cards_per_player

def test_deal_and_print_cards_removing_from_deck():
    """Tests that _deal_and_print_cards() removes cards from the deck."""
    card_deck = CardDeck()
    _, players_cards = game._setup_players_and_card_lists()
    game._deal_and_print_cards(card_deck, players_cards, column_width=0)

    remaining_cards = card_deck.get_card_count()
    standard_deck_count = 52
    expected_remaining_cards = standard_deck_count - (game.CARDS * game.PLAYERS)

    assert remaining_cards == expected_remaining_cards

def test_get_and_print_scores():
    """Tests that _get_and_print_scores() function works properly."""
    cards = [[('Diamonds','Queen'), ('Hearts','2')],
             [('Hearts','1'), ('Clubs','Ace'), ('Spades','Jack')]]
    scores = game._get_and_print_scores(cards, column_width=0)
    expected_scores = [30, 18]
    assert scores == expected_scores

def test_get_and_print_winners1(capfd):
    """Tests that _get_and_print_winners() works when first player wins."""
    players = ['1', '2']
    scores = [50, 49]
    game._get_and_print_winners(players, scores)
    print_output, _ = capfd.readouterr()
    assert print_output == '1 Wins!!!\n'

def test_get_and_print_winners2(capfd):
    """Tests that _get_and_print_winners() works when second player wins."""
    players = ['bill', 'jim']
    scores = [50, 51]
    game._get_and_print_winners(players, scores)
    print_output, _ = capfd.readouterr()
    assert print_output == 'jim Wins!!!\n'

def test_get_and_print_winners_tie1(capfd):
    """Tests that _get_and_print_winners() works when 2 out of 3 players tie for high score."""
    players = ['1', '2', '3']
    scores = [20, 19, 20]
    game._get_and_print_winners(players, scores)
    print_output, _ = capfd.readouterr()
    assert print_output == '1 and 3 Tie!!!\n'

def test_get_and_print_winners_tie2(capfd):
    """Tests that _get_and_print_winners() works when 3 players tie."""
    players = ['mikie', '2', '4a']
    scores = [3, 3, 3]
    game._get_and_print_winners(players, scores)
    print_output, _ = capfd.readouterr()
    assert print_output == 'mikie and 2 and 4a Tie!!!\n'

def test_get_print_column_width():
    """Tests that the correct width is returned from _get_print_column_width()."""
    phrases = ['1234', '123456']
    print_column_width = game._get_print_column_width(phrases,
                                                      column_padding=2)
    expected_print_column_width = 8
    assert print_column_width == expected_print_column_width

def test_print_list_as_columns(capfd):
    """Tests that _print_list_as_columns() prints as expected."""
    phrases = ['test phrase', 'test']
    game._print_list_as_columns(phrases, column_width=12)
    print_output, _ = capfd.readouterr()
    assert print_output == 'test phrase test        \n'

def test_setup_players_and_card_lists():
    """Tests that _setup_players_and_card_lists() creates players and players cards lists."""
    players, players_cards = game._setup_players_and_card_lists()

    expected_players_count = game.PLAYERS
    is_correct_players_count = (len(players) == expected_players_count)

    expected_card_lists = game.PLAYERS
    is_correct_card_list_size = (len(players_cards) == expected_card_lists)

    assert is_correct_players_count and is_correct_card_list_size
