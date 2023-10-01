from random import choice
from blight.math_utils import distance
from .generate_dungeon import FLOOR


def find_start_positions(dungeon, n):
    # Find all the ' ' tiles
    empty_tiles = [
        (x, y)
        for y, row in enumerate(dungeon)
        for x, cell in enumerate(row)
        if cell == FLOOR
    ]

    # Initialize list for starting positions
    start_positions = []

    # If there are fewer empty tiles than the number of starting positions, return all empty tiles
    if len(empty_tiles) <= n:
        return empty_tiles

    # Pick the first starting position randomly
    start_positions.append(choice(empty_tiles))

    for _ in range(n - 1):
        farthest_point = None
        max_distance = -1

        # Find a point that is as far as possible from all other starting points
        for point in empty_tiles:
            min_distance_to_start = min(
                distance(point, start_point) for start_point in start_positions
            )

            if min_distance_to_start > max_distance:
                max_distance = min_distance_to_start
                farthest_point = point

        if farthest_point:
            start_positions.append(farthest_point)
            empty_tiles.remove(farthest_point)

    return start_positions
