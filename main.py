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

LOSE_HUNGER = """

YOUR STOMACH IS EMPTY.
WHO KNEW THAT WHAT THE DOCTOR SAID WAS TRUE,
THAT HUMAN ROBOT HYBRIDS WOULD NEED 
TOFU TO SUSTAIN THEMSELVES.
YOUR ROBOT SYSTEMS START TO SHUT DOWN.
YOUR HUMAN EYES CLOSE.
THE LAST THING THAT YOU HEAR ARE SIRENS.
THEY GOTCHU. THEY GOT THE CAR.
WE FAILED...

----- GAME OVER -----
"""

LOSE_AGENTS = """
THE AGENTS HAVE CLOSED IN ON YOU.
THERE ARE AT LEAST 20 CARS SURROUNDING YOU.
THE LEAD CAR BUMPS YOUR PASSENGER SIDE.
YOU MANAGE TO CORRECT YOUR STEERING TO KEEP YOU FROM CRASHING.

YOU DIDN'T SEE THE AGENTS CAR BESIDE YOU.
THE DRIVER BUMPS YOUR CAR.
AND THAT'S IT.

YOU SPIN OUT OF CONTROL.
THE CAR FLIPS OVER AT LEAST 2 TIMES.
OR MORE... YOU LOST COUNT.

SIRENS.

"ARE THEY ALIVE?" SOMEONE ASKS.
"DOESN'T MATTER. ALL WE WANTED WAS THE CAR."
YOU SEE A DOG WALKING OUT OF THE CAR.
"WAS IT IN THE CAR THE WHOLE TIME?" YOU 
THINK TO YOURSELF.

THE DOG LOOKS UP AT THE OFFICERS.
"YOU WILL NEVER STOP THE REVOLUTION."
"DID THE DOG JUST TALK?" YOU THINK TO YOURSELF.

YOU DRIFT OFF INTO UNCONSCIOUSNESS.

----- GAME OVER -----
"""

LOSE_FUEL = """
YOUR CAR BEGINS TO SLOW DOWN.
YOU PUT THE PETAL TO THE METAL.
NOTHING HAPPENS. YOU KEEP SLOWING DOWN.
YOU DON'T KNOW WHATS HAPPENING.

THEN YOU CHECK YOUR FUEL.
YOU TANK IS EMPTY. THERES NOTHING YOU CAN DO.
YOU HEAR THE DISTANT SIRENS APPROACHING.

YOU TRY AND MAKE A RUN FOR IT.
BUT THEY CATCH YOU. IT'S OVER.
THEY GOT THE CAR. 
AND YOU...

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
    TOFU_CHANCE = 0.03

    # Variables
    done = False

    km_traveled = 0
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
            break
        elif hunger > 45:
            # Lose - too hungry
            # Print losing hunger scenario
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            break
        elif agents_distance >= 0:
            # Lose - too agents
            # Print agent loss scenario
            type_text_output(LOSE_AGENTS)
            break
        elif fuel <= 0:
            # Lose - too fuel
            # Print fuel loss scenario
            type_text_output(LOSE_FUEL)
            break

        # Random events
        # Fido
        if random.random() < TOFU_CHANCE:
            # Fido pops up says something and refills tofu
            tofu = MAX_TOFU_LEVEL
            print()
            print("******** Your tofu is magically refilled!")
            print("******** \"You're welcome!\" a voice says.")
            print("******** It's Fido.")
            print("******** He's using his tofu cooking skills.")

        # Showing Hunger
        if hunger > 35:
            print("******** You are starving. You should Eat soon.")
        elif hunger > 20:
            print("******** You can hear your stomach growling...")

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

        # Upkeep - increase hunger and turn counter
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)
            turns += 1

        # Pause
        time.sleep(1.2)

    # Outroduction
    print("Thanks for playing! Please play again. =)")
    print(f"You finished the game in {turns} turns.")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
