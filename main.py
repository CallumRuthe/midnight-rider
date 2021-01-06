# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars... out of 100.

import random
import sys
import textwrap
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
    C. Speed ahead at full throttle.
    D. Stop for fuel at a refueling station.
       (No food available)
    E. Status Check
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
    # intro()

    # Constants
    MAX_FUEL_LEVEL = 50
    MAX_TOFU_LEVEL = 3

    # Variables
    done = False

    km_traveled = 0             # 100km traveled is the goal
    agents_distance = -20.0
    turns = 0                   # amount of turns taken
    tofu = MAX_TOFU_LEVEL
    fuel = MAX_FUEL_LEVEL
    hunger = 0                  # hunger increases with num

    while not done:
        # TODO:  Check if reached END GAME

        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if users_choice == "c":
            # Drive fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn Fuel
            fuel -= random.randrange(5, 11)

            # Player distance travelled
            km_traveled += player_distance_now

            # Agent's distance travelled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to player
            print()
            print(f"-------- You sped ahead {player_distance_now} kms!")
            print()
        elif users_choice == "d":
            # Refuel
            # Fill the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give the user feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print()

        elif users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm traveled: {km_traveled} km")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind you.")
            print(f"\tYou have {tofu} tofu left.")
            print(f"\t------------------\n")
        elif users_choice == "q":
            done = True

        # Pause
        time.sleep(1)

        # TODO: Change the environment based on choice and RNG

    # Outroduction
    print("Thanks for playing! Please play again. =)")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
