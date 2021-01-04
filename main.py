# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars... out of 100.

import textwrap
import sys
import time


INTRODUCTION = """

WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THE GOVERNMENT WANTS IT FOR THEIR GAIN.

WE CANT LET THAT HAPPEN.

ONE GOAL: SURVIVAL... AND THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU.

"""

CHOICES = """
    ----
    Q. QUIT
    ----
"""


def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    intro()

    done = False

    while not done:
        # TODO:  Check if reached END GAME

        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")
        if users_choice == "q":
            done = True

        # TODO: Change the environment based on choice and RNG

    # Outroduction
    print("Thanks for playing! Please play again. =)")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
