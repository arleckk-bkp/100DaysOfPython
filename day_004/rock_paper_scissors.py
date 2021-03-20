import random

import paper
import rock
import scissor


def get_option(choice):
    if choice == "0":
        return rock.rock
    elif choice == "1":
        return paper.paper
    else:
        return scissor.scissors


def who_wins(player_choice, computer_choice):
    WIN = "You win"
    LOSE = "You lose"
    DRAW = "Draw"
    if player_choice == "0":
        if computer_choice == "0":
            return DRAW
        elif computer_choice == "1":
            return LOSE
        else:
            return WIN
    elif player_choice == "1":
        if computer_choice == "0":
            return WIN
        elif computer_choice == "1":
            return DRAW
        else:
            return LOSE
    else:
        if computer_choice == "0":
            return LOSE
        elif computer_choice == "1":
            return WIN
        else:
            return DRAW


player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
print(get_option(player_choice))
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(get_option(str(computer_choice)))
print(who_wins(player_choice, str(computer_choice)))
