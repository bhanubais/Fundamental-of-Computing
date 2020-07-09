"""
[Project Description](https://www.coursera.org/learn/interactive-python-1/supplement/ijRP5/mini-project-description)
"""
from random import randrange
names = ["rock", "Spock", "paper", "lizard", "scissors"]
def name_to_number(name):
    return names.index(name)

def number_to_name(number):
    return names[number]

def rpsls(player_choice):
    # part 1
    print()
    print(f"Player chooses {player_choice}")
    player_number = name_to_number(player_choice)

    # part 2
    comp_number = randrange(5)
    comp_choice = number_to_name(comp_number)
    print(f"Computer chooses {comp_choice}")

    # part 3
    diff = (player_number - comp_number) % 5
    if diff == 0:
        print("This is a Tie")
        return
    elif diff == 1 or diff == 2:
        print("Player wins!")
        return
    else:
        print("Computer wins!")
        return

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
