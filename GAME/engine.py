import random


class Card:
    def __init__(self, name, value, effect):
        self.name = name
        self.value = value
        self.effect = effect

    def __str__(self):
        return f"{self.name} (Value: {self.value})"


class Player:
    def __init__(self, name):
        """
        Method to initialize a player

        Attributes: The name of the player
        Returns: None
        """
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        """
        Method to draw a card from the deck

        Attributes: The deck to draw from
        Returns: None
        """
        self.hand.append(deck.draw())

    def play_card(self, card_index):
        """
        Method to play a card from the player's hand

        Attributes: The index of the card to play
        Returns: The card that was played
        """
        return self.hand.pop(card_index)


class Deck:
    def __init__(self):
        """
        Method to initialize a deck of cards

        Attributes: None
        Returns: None
        """
        self.cards = [
            Card("Guard", 1, "Guess a player's hand"),
            Card("Priest", 2, "Look at a player's hand"),
            Card("Baron", 3, "Compare hands wi1th another player"),
            Card("Handmaid", 4, "Protection until next turn"),
            Card("Prince", 5, "Discard a player's hand"),
            Card("King", 6, "Trade hands with another player"),
            Card("Countess", 7, "Must be discarded if caught with King or Prince"),
            Card("Princess", 8, "Lose if discarded"),
        ] * 2  # Two of each card for simplicity
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None
