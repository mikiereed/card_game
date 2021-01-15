import pytest
import src.game as game

def test_deal_and_print_cards():
    pass

def test_get_print_column_width():
    phrases = ['1234', '123456']
    print_column_width = game._get_print_column_width(phrases,
                                                      column_padding=2)
    expected_print_column_width = 8
    assert print_column_width == expected_print_column_width

def test_play_game():
    pass

def test_set_up_players_and_card_lists():
    players, players_cards = game._set_up_players_and_card_lists()

    expected_players_count = game.PLAYERS
    is_correct_players_count = (len(players) == expected_players_count)

    expected_card_lists = game.PLAYERS
    is_correct_card_list_size = (len(players_cards) == expected_card_lists)

    assert is_correct_players_count and is_correct_card_list_size

