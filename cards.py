"""Contains all code for constructing a deck of cards.
"""

SUITS = ("Hearts", "Spades", "Diamonds", "Clubs")
RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")


class Card:
    """A card from a French deck with a rank and suit.

    Rank: 2 - Ace
    Suit: Hearts, Diamonds, Clubs, Spades
    """

    def __init__(self, rank, suit):
        self.Rank = rank
        self.Suit = suit

    def getValue(self):
        return f"{self.Rank} of {self.Suit}"

    def shuffle(self):
        pass
