from src.card import Card

def test_card():
    card = Card(1, 'heart')
    assert type(card) == Card