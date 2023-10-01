import random
from termcolor import colored
from .copy_dungeon import copy_dungeon
from .generate_dungeon import Tile

CLEAR_SCREEN = "\033c"

COLORS = {
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
}

TILE_TEXT_MAP = {
    Tile.FLOOR: " ",
    Tile.WALL: "▓",
    Tile.PWALL: "#",
}

TILE_COLOR_MAP = {
    Tile.FLOOR: "black",
    Tile.WALL: "dark_grey",
    Tile.PWALL: "white",
}

TILE_ON_COLOR_MAP = {
    Tile.FLOOR: "on_black",
    Tile.WALL: "on_black",
    Tile.PWALL: "on_black",
}


def determine_player_colors(num_players):
    # Create a list of all available colors
    available_colors = list(COLORS.keys())
    while len(available_colors) < num_players:
        available_colors += list(COLORS.keys())

    # Shuffle the list of available colors
    random.shuffle(available_colors)

    # Return the first num_players colors
    return available_colors[:num_players]


def print_cell(cell: Tile | str):
    if isinstance(cell, Tile):
        return colored(
            text=TILE_TEXT_MAP[cell],
            color=TILE_COLOR_MAP[cell],
            on_color=TILE_ON_COLOR_MAP[cell],
        )
    else:
        return cell


def print_dungeon(dungeon=[], starts=None):
    # print(CLEAR_SCREEN)

    # Create a dictionary mapping starts to randomly selected colors using list comprehension
    colors = determine_player_colors(len(starts))
    copy = copy_dungeon(dungeon)

    print(f'{colored("Players", "red")}:')
    player_num = 1
    for i, (x, y) in enumerate(starts):
        color = colors[i]
        print(
            colored(
                f"  - player_{player_num} ({color})",
                color,
            )
        )
        copy[y][x] = colored("@", color, on_color=TILE_ON_COLOR_MAP[Tile.FLOOR])
        player_num += 1

    dungeon_str = "\n".join("".join(print_cell(cell) for cell in row) for row in copy)
    print(f'{colored("Dungeon Map", "red")}:')
    print(dungeon_str)
