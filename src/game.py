from src.card_deck import CardDeck

CARDS = 3
NAN_VALUES_SCORING = {'Ace': 1, 'Jack': 11, 'Queen': 12, 'King': 13}
PLAYERS = 2
SUIT_SCORING = {'Clubs': 4, 'Hearts': 3, 'Diamonds': 2, 'Spades': 1}

def play_game():
    is_keep_playing = True
    while is_keep_playing:
        card_deck = CardDeck(shuffled=True)
        players, players_cards = _set_up_players_and_card_lists()

        print_column_width = _get_print_column_width(phrases=card_deck.cards,
                                                     column_padding=3)
        _print_list_as_columns(players, print_column_width)
        _deal_and_print_cards(card_deck, players_cards, print_column_width)
        scores = _get_and_print_scores(players_cards, print_column_width)
        _get_and_print_winners(players, scores)

        keep_playing = input("Do you want to play again? y/n: ")
        if keep_playing.startswith('n'):
            is_keep_playing = False

def _deal_and_print_cards(card_deck, players_cards, column_width):
    for i in range(CARDS):
            cards_pulled = []
            for i, _ in enumerate(players_cards):
                card_pulled = card_deck.pull_card_from_deck()
                players_cards[i].append(card_pulled)
                cards_pulled.append(str(card_pulled))
            _print_list_as_columns(cards_pulled, column_width)

def _get_and_print_scores(players_cards, column_width):
    scores = _get_scores(players_cards)
    scores_str = [f'Score: {score}' for score in scores]
    _print_list_as_columns(scores_str, column_width)
    return scores

def _get_and_print_winners(players, scores):
    winners = _get_winner(players, scores)
    _print_winners(winners)
    return winners

def _get_card_score(card):
    suit_score = SUIT_SCORING[card[0]]
    try:
        value_score = int(card[1])
    except ValueError:
        value_score = NAN_VALUES_SCORING[card[1]]
    return suit_score * value_score

def _get_print_column_width(phrases, column_padding):
    longest_phrase = max(len(str(phrase)) for phrase in phrases)
    column_width = longest_phrase + column_padding
    return column_width

def _get_scores(players_cards):
    scores = []
    for i, player_cards in enumerate(players_cards):
        scores.append(0)
        for card in player_cards:
            scores[i] += _get_card_score(card)
    return scores

def _get_winner(players, scores):
    # if multiple winners, it's a tie
    winners = [players[i] for i, x in enumerate(scores) if x == max(scores)]
    return winners

def _print_list_as_columns(list_to_print, column_width):
    print("".join(element.ljust(column_width) for element in list_to_print))

def _print_winners(winners):
    if len(winners) == 1:
        print(f'{winners[0]} Wins!!!')
    else:
        winners_str = " and ".join(winners)
        print(f'{winners_str} Tie!!!')

def _set_up_players_and_card_lists():
    players = [f'Player {i + 1}' for i in range(PLAYERS)]
    players_cards = []
    for _ in players:
        players_cards.append([])
    return players, players_cards

if __name__ == "__main__":
    play_game()