from random import randint, choice

"""
Monty Hall Problem Simulation

This script simulates the Monty Hall problem, where a player must choose between 3 doors:
- Behind one door is a prize (car).
- Behind the other two doors are goats.

After the player chooses a door, the host (Monty) opens one of the other doors, which always reveals a goat. 
The player is then given the option to switch to the remaining unopened door or stick with their original choice.

### Key Insight:
Contrary to natural intuition, the optimal strategy is to **switch doors** after Monty opens a door. 
The reason is that if the player sticks with their original choice, the chance of winning is only **1/3**. 
However, if the player switches, their chance of winning increases to **2/3**. 
This means that there is a **higher probability of success by switching doors**!

The player's strategy can be:
- Always "switch" doors after Monty opens a door.
- Always "stay" with the originally chosen door.
- Choose randomly between "switching" or "staying."

The simulation runs for a specified number of rounds (`NUM_OF_ROUNDS`) and calculates the percentage of wins for the chosen strategy.

Parameters:
    NUM_OF_ROUNDS (int): The number of rounds to simulate (default is 1,000,000).
    PLAYER_STRATEGY (str): The player's strategy during the simulation. 
        Options:
        - "switch": Player always switches to the other door after Monty reveals a goat.
        - "stay": Player always stays with their original choice.
        - "random": Player randomly chooses whether to switch or stay.

Functions:
    play_round(): Simulates one round of the game and returns 1 for success (player wins the car) or 0 for failure (player gets a goat).

Variables:
    success_count (int): Total number of successful rounds (where the player wins the car).

Output:
    The program prints the success rate (percentage) of the player's strategy after running the simulation for `NUM_OF_ROUNDS`.
"""

NUM_OF_ROUNDS = 1000000
PLAYER_STRATEGY = "switch"  # switch/stay/random


def play_round():  # returns 0 for failure, 1 for success
    prize_door = randint(1, 3)
    player_door = randint(1, 3)
    monty_door = choice([door for door in [1, 2, 3] if
                         not door in [prize_door, player_door]])  # if two doors are possible, choose uniformly
    remaining_door = 6 - (player_door + monty_door)  # 1 + 2 + 3 = 6
    player_door = {"switch": remaining_door, "stay": player_door, "random": choice([remaining_door, player_door])}[
        PLAYER_STRATEGY]
    return 1 if (player_door == prize_door) else 0


success_count = sum([play_round() for round_num in range(NUM_OF_ROUNDS)])
print((100.0 * success_count) / NUM_OF_ROUNDS)
