import random


def roll_dice():
    return random.randint(1, 6)


def play_round():
    player1_score = roll_dice()
    player2_score = roll_dice()

    print("Player 1 rolls:", player1_score)
    print("Player 2 rolls:", player2_score)

    if player1_score > player2_score:
        print("Player 1 wins this round!")
        return 1
    elif player2_score > player1_score:
        print("Player 2 wins this round!")
        return 2
    else:
        print("It's a tie for this round!")
        return 0


def main():
    print("Welcome to the Dice Game!")
    rounds = int(input("Enter the number of rounds to play: "))

    player1_wins = 0
    player2_wins = 0
    ties = 0

    for round in range(1, rounds + 1):
        print(f"\nRound {round}:")

        winner = play_round()
        if winner == 1:
            player1_wins += 1
        elif winner == 2:
            player2_wins += 1
        else:
            ties += 1

    print("\nGame Over!")
    print(f"Player 1 wins: {player1_wins} rounds")
    print(f"Player 2 wins: {player2_wins} rounds")
    print(f"Ties: {ties} rounds")


if __name__ == "__main":
    main()