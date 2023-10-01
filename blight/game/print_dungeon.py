from termcolor import colored
from .copy_dungeon import copy_dungeon
from .generate_dungeon import FLOOR, WALL

CLEAR_SCREEN = "\033c"

COLORS = {
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
}

import random


def determine_player_colors(num_players):
    # Create a list of all available colors
    available_colors = list(COLORS.keys())
    while len(available_colors) < num_players:
        available_colors += list(COLORS.keys())

    # Shuffle the list of available colors
    random.shuffle(available_colors)

    # Return the first num_players colors
    return available_colors[:num_players]



def print_cell(tile):
    if tile == FLOOR:
        return colored(" ")
    elif tile == WALL:
        return colored("█", "dark_grey")
    else:
        return tile

def print_dungeon(dungeon=[], starts=None):
    # print(CLEAR_SCREEN)

    # Create a dictionary mapping starts to randomly selected colors using list comprehension
    colors = determine_player_colors(len(starts))
    copy = copy_dungeon(dungeon)

    print(f'{colored("Players", "red")}:')
    player_num = 1
    for i, (x, y) in enumerate(starts):
        color = colors[i]
        print(colored(f"  - player_{player_num} ({color})", color, attrs=["bold"]))
        copy[y][x] = colored("𓀠", color, attrs=["bold"])
        player_num += 1

    dungeon_str = "\n".join("".join(print_cell(cell) for cell in row) for row in copy)
    print(f'{colored("Dungeon Map", "red")}:')
    print(dungeon_str)
