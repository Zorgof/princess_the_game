from GAME.engine import Deck, Player

""" Main game loop """


def main():
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    player1.draw_card(deck)
    player2.draw_card(deck)

    current_player = player1
    other_player = player2

    while deck.cards:
        print(f"\n{current_player.name}'s turn")
        current_player.draw_card(deck)
        print(f"Your hand: {[str(card) for card in current_player.hand]}") #

        while True:
            try:
                card_index = int(
                    input(f"Choose a card to play (0-{len(current_player.hand) - 1}): ")
                )
                if 0 <= card_index < len(current_player.hand):
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        played_card = current_player.play_card(card_index)
        print(f"{current_player.name} played {played_card}")

        if played_card.name == "Princess":
            print(f"{current_player.name} discarded the Princess and lost!")
            break

        current_player, other_player = other_player, current_player

    print("Game over!")


if __name__ == "__main__":
    main()
