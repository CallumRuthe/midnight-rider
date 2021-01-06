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


WIN = """

You pressed the button to open the gate.
This isn't the first time you've done this, 
so you know how to time it exactly.
Just as the doors close, you slide right into HQ.
You know you did the right thing, the government 
would have just torn the car apart.
They don't know its secrets...
that it holds the key to different worlds.
As you step out of the vehicle, Fido runs up to you.
"Thank you for saving me," he says.
As you take a couple of steps away from the car,
it makes a strange sound.
It changes shape.
You've seen it before, but only on TV.
"...Bumblebee???"

----- GAME OVER -----
"""

CHOICES = """
    ----
    A. Eat a tofu.
    B. Drive ahead at a moderate speed.
    C. Speed ahead at full throttle.
    D. Stop for fuel at a refueling station.
       (No food available)
    E. Status Check
    Q. QUIT
    ----
"""


def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    # type_text_output(INTRODUCTION)

    # Constants
    MAX_FUEL_LEVEL = 50
    MAX_TOFU_LEVEL = 3
    MAX_DISTANCE_TRAVELLED = 100

    # Variables
    done = False

    km_traveled = 99
    agents_distance = -20.0
    turns = 0
    tofu = MAX_TOFU_LEVEL
    fuel = MAX_FUEL_LEVEL
    hunger = 0

    while not done:
        # Check if reached END GAME
        if km_traveled >= MAX_DISTANCE_TRAVELLED:
            # Win
            # Print win scenario (stylistic typing)
            time.sleep(2)
            type_text_output(WIN)

            # Break from while loop
            break

        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if users_choice == "a":
            # Eat
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmmmmmm. Soy bean goodness.")
                print("-------- Your hunger is sated.")
                print()
            else:
                print()
                print("-------- You have none left")
                print()
        elif users_choice == "b":
            # Drive moderately
            player_distance_now = random.randrange(7, 15)
            agents_distance_now = random.randrange(7, 15)

            # Burn Fuel
            fuel -= random.randrange(2, 6)

            # Player distance travelled
            km_traveled += player_distance_now

            # Agent's distance travelled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to player
            print()
            print(f"-------- You drove ahead {player_distance_now} kms.")
            print()
        elif users_choice == "c":
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

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5,13)

        # Update user about hunger level
            if hunger > 37:
                print()
                print("-------- You are starving. You should Eat soon.")
                print()
            elif hunger > 25:
                print()
                print("-------- You can hear your stomach growling...")
                print()

        # Pause
        time.sleep(1.2)

    # Outroduction
    print("Thanks for playing! Please play again. =)")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
