# Author: Robert Brumleve
# GitHub username: robert-brumleve
# Date: 2022-08-20
# Description: A program that contains a Card class and Deck class for playing cards.

import random


class Card:
    """
    Represents a playing card. Has data members for the rank and the suit.
    Methods:
    get_rank
    get_suit
    """

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_rank(self):
        """
        Takes no parameters. Returns the rank of the card.
        Rank: A,1,2,3,4,5,6,7,8,9,10,J,Q,K
        """

        return self._rank

    def get_suit(self):
        """
        Takes no parameters. Returns the suit of the card.
        Suit: ♥,♣,♦,♠
        """

        return self._suit


class Deck:
    """
    Represents a deck of cards. Has a data member for the deck.
    Methods:
    get_deck
    set_deck
    set_suit_of_cards
    print_deck
    shuffle_deck
    """

    def __init__(self):
        self._deck = self.set_deck()

    def get_deck(self):
        """
        Takes no parameters. Returns the deck as a list of cards.
        """

        return self._deck

    def set_deck(self):
        """
        Takes no parameters. Creates the deck of cards when initializing.
        """

        deck = []

        for card in self.set_suit_of_cards("♥"):
            deck.append(card)
        for card in self.set_suit_of_cards("♣"):
            deck.append(card)
        for card in self.set_suit_of_cards("♦"):
            deck.append(card)
        for card in self.set_suit_of_cards("♠"):
            deck.append(card)

        #jokers = -1
        #while jokers < 0:
        #    try:
        #        jokers = int(input("How many jokers?"))
        #        if jokers < 0:
        #            print("Must be positive integer.")
        #    except ValueError:
        #        print("Invalid input. Enter an integer.")

        #for j in range(jokers):
        #    deck.append(Card("Joker", ""))

        return deck

    def set_suit_of_cards(self, suit):
        """
        Takes one parameter: suit is the suit of the card.
        Creates cards A-K or K-A, depending on the suit.
        """

        suit_of_cards = []

        if suit == "♥" or suit == "♣":

            suit_of_cards.append(Card("A", suit))
            # Append cards 2-10
            for i in range(9):
                suit_of_cards.append(Card(str(i+2), suit))
            suit_of_cards.append(Card("J", suit))
            suit_of_cards.append(Card("Q", suit))
            suit_of_cards.append(Card("K", suit))

        elif suit == "♦" or suit == "♠":

            i = 10
            suit_of_cards.append(Card("K", suit))
            suit_of_cards.append(Card("Q", suit))
            suit_of_cards.append(Card("J", suit))
            # Append cards 10-2
            while i > 1:
                suit_of_cards.append(Card(str(i), suit))
                i -= 1
            suit_of_cards.append(Card("A", suit))

        return suit_of_cards

    def print_deck(self):
        """
        Takes no parameters. Prints each card in the deck.
        """

        for card in self._deck:
            print(card.get_rank(), card.get_suit())

    def shuffle_deck(self):
        """
        Takes no parameters. Shuffles the deck by appending random cards to a new list.
        """

        shuffled_deck = []
        i = len(self._deck)

        while i > 0:
            j = random.randrange(i)
            shuffled_deck.append(self._deck[j])
            del self._deck[j]
            i -= 1

        self._deck = shuffled_deck


def main():
    deck1 = Deck()
    deck1.shuffle_deck()
    deck1.print_deck()


if __name__ == "__main__":
    main()
