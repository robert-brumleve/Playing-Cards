# Author: Robert Brumleve
# GitHub username: robert-brumleve
# Date: 2022-08-22
# Description: A program that a player can play Old Maid with computer players.

import random
import playing_cards


class Player:
    """
    Represents a player playing Old Maid. Has data members for player number and cards in their hand.
    Methods:
    get_number
    get_hand
    set_hand
    shuffle_hand
    print_hand
    check_for_dealt_pairs
    check_for_pairs
    """

    def __init__(self, number):
        self._number = number
        self._hand = []

    def get_number(self):
        """
        Takes no parameters.
        Returns the player number.
        """

        return self._number

    def get_hand(self):
        """
        Takes no parameters.
        Returns the player's hand.
        """

        return self._hand

    def add_card(self, card):
        """
        Takes one parameter: card is the card to add to the player's hand.
        Appends a card to the player's hand.
        """

        self._hand.append(card)

    def remove_card(self, card):
        """
        Takes one parameter: card is the card to remove from the player's hand.
        Removes a card from the player's hand.
        """

        self._hand.remove(card)

    def shuffle_hand(self):
        """
        Takes no parameters.
        Shuffles the cards in a player's hand.
        """

        shuffled_hand = []
        i = len(self._hand)

        while i > 0:
            j = random.randrange(i)
            card = self._hand[j]
            del self._hand[j]
            shuffled_hand.append(card)
            i -= 1

        self._hand = shuffled_hand

    def print_hand(self):
        """
        Takes no parameters.
        Prints each card in a player's hand.
        """

        hand = []
        for c in self._hand:
            card = c.get_rank(), c.get_suit()
            hand.append(card)
        print(hand)

    def check_for_dealt_pairs(self):
        """
        Takes no parameters.
        Checks for pairs after dealing cards and removes the pairs from the players' hands.
        """

        i = 0
        while i < len(self._hand):
            j = 0
            while j < len(self._hand):
                if self._hand[i] != self._hand[j] and self._hand[i].get_rank() == self._hand[j].get_rank():
                    del self._hand[i]
                    del self._hand[j-1]
                    j = 0
                    if i >= len(self._hand):
                        i -= 2
                else:
                    j += 1
            i += 1

    def check_for_pairs(self, card):
        """
        Takes one parameter. card is the card to check.
        Checks a player's hand for a card with equal rank to card parameter
        and removes the two cards from the player's hand.
        """

        i = 0
        while i < len(self._hand):
            if self._hand[i] != card and self._hand[i].get_rank() == card.get_rank():
                del self._hand[i]
                self._hand.remove(card)
            i += 1


class OldMaid:
    """
    Represents a game of Old Maid.
    Methods:
    get_deck
    get_player_by_number
    set_players
    set_current_players
    deal_cards
    get_index
    play_game
    """

    def __init__(self):
        self._players = self.set_players()
        self._deck = playing_cards.Deck()
        self._current_players = []

    def get_deck(self):
        """
        Takes no parameters.
        Returns the deck of cards.
        """

        return self._deck

    def get_player_by_number(self, number):
        """
        Takes one parameter: number is the player number.
        Returns the Player object with the given number.
        """

        return self._players[number - 1]

    def set_players(self):
        """
        Takes no parameters.
        Makes a list of Player objects.
        Amount is determined by user input.
        """

        players_list = []
        players = 0

        while players < 2 or players > 10:
            try:
                players = int(input("How many players? (2-10)"))
                if players < 2:
                    print("Not enough players.")
                if players > 10:
                    print("Too many players.")
            except ValueError:
                print("Invalid input. Enter an integer.")

        for p in range(players):
            players_list.append(Player(p + 1))
        return players_list

    def set_current_players(self):
        """
        Takes no parameters.
        Makes a list of Player objects currently playing.
        """

        for p in self._players:
            self._current_players.append(p)

    def deal_cards(self):
        """
        Takes no parameters.
        Deals cards to each player one by one, if a card is available.
        """

        cards = len(self._deck.get_deck())

        while cards > 0:
            for p in self._players:
                if cards > 0:
                    p.add_card(self._deck.get_deck()[0])
                    del self._deck.get_deck()[0]
                    cards -= 1

    def get_index(self):
        """
        Takes no parameters.
        Gets the index of the first player in the current_players list that has at least one card.
        """

        i = 0
        while i < len(self._current_players):
            if len(self._current_players[i].get_hand()) > 0:
                return i
            i += 1

    def play_game(self):
        """
        Takes no parameters.
        Plays a game of Old Maid.
        """

        # Game setup
        joker_card = playing_cards.Card("Joker", "")
        self._deck.get_deck().append(joker_card)
        self._deck.shuffle_deck()
        self.deal_cards()
        for p in self._players:
            p.check_for_dealt_pairs()
        self.set_current_players()

        while len(self._current_players) > 1:
            i = 0
            for p in self._current_players:
                if len(self._current_players) > 1:

                    # User's turn
                    if p == self._players[0] and len(p.get_hand()) > 0:
                        drawn_card_index = -1
                        while drawn_card_index < 0 or drawn_card_index > len(self._current_players[1].get_hand()):
                            try:
                                drawn_card_index = int(input(f"Draw a card from the next player. (1-{len(self._current_players[1].get_hand())})"))
                                if drawn_card_index < 1 or drawn_card_index > len(self._current_players[1].get_hand()):
                                    print(f"Input must be within range 1-{len(self._current_players[1].get_hand())}.")
                            except ValueError:
                                print("Invalid input. Enter an integer.")
                        drawn_card = self._current_players[1].get_hand()[drawn_card_index - 1]
                        print(f"You took {drawn_card.get_rank()} {drawn_card.get_suit()} from Player {self._current_players[1].get_number()}")
                        self._current_players[0].add_card(drawn_card)
                        self._current_players[1].remove_card(drawn_card)

                    # Last player's turn
                    elif p == self._current_players[len(self._current_players) - 1]:
                        j = self.get_index()
                        drawn_card_index = random.randrange(len(self._current_players[j].get_hand()))
                        drawn_card = self._current_players[j].get_hand()[drawn_card_index]
                        if self._current_players[j] == self._players[0]:
                            print(f"Player {p.get_number()} took your {drawn_card.get_rank()} {drawn_card.get_suit()}.")
                        self._current_players[len(self._current_players) - 1].add_card(drawn_card)
                        self._current_players[j].remove_card(drawn_card)

                    # All other player's turns
                    else:
                        drawn_card_index = random.randrange(len(self._current_players[i+1].get_hand()))
                        drawn_card = self._current_players[i+1].get_hand()[drawn_card_index]
                        self._current_players[i].add_card(drawn_card)
                        self._current_players[i+1].remove_card(drawn_card)
                p.check_for_pairs(drawn_card)
                i += 1

            # Remove players from current_players list if they don't have any cards
            i = 0
            for p in self._current_players:
                if len(p.get_hand()) == 0:
                    del self._current_players[i]
                i += 1

            # Print user's hand and amount of cards each other player has
            self._players[0].print_hand()
            for p in self._current_players:
                if p != self._players[0]:
                    if len(p.get_hand()) > 1:
                        print(f"Player {p.get_number()} has {len(p.get_hand())} cards.")
                    else:
                        print(f"Player {p.get_number()} has 1 card.")
                    p.shuffle_hand()

        # Game over
        print(f"Player {self._current_players[0].get_number()} is the Old Maid!")


OM = OldMaid()
OM.play_game()
