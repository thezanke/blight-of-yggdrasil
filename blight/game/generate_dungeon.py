from enum import Enum
from math import sqrt
import random


class Tile(Enum):
    PWALL = 0
    WALL = 1
    FLOOR = 2


def find_densest_area(dungeon, width, height, subgrid_size=5):
    max_walls = 0
    dense_x, dense_y = 0, 0

    for x in range(1, width - subgrid_size):
        for y in range(1, height - subgrid_size):
            walls = sum(
                dungeon[y + dy][x + dx] == Tile.WALL
                for dy in range(subgrid_size)
                for dx in range(subgrid_size)
            )
            if walls > max_walls:
                max_walls = walls
                dense_x, dense_y = x, y

    return dense_x + subgrid_size // 2, dense_y + subgrid_size // 2


def add_caverns(dungeon, width, height, room_count):
    print(f"Generating {room_count} rooms...")

    cavern_origins = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(room_count):
        if cavern_origins:
            # Find the next densest area to start the new room
            x, y = find_densest_area(dungeon, width, height)
        else:
            # For the first room, start randomly
            x, y = random.randint(1, width - 2), random.randint(1, height - 2)

        cavern_origins.append((x, y))

        for _ in range(width * height // 10):  # Number of steps to hollow out the room
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy

            if 0 < new_x < width - 1 and 0 < new_y < height - 1:
                dungeon[new_y][new_x] = Tile.FLOOR
                x, y = new_x, new_y

    return cavern_origins


def are_points_connected(dungeon, start, end):
    stack = [start]
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while stack:
        x, y = stack.pop()

        if (x, y) == end:
            return True

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(dungeon[0]) and 0 <= new_y < len(dungeon):
                if (
                    dungeon[new_y][new_x] == Tile.FLOOR
                    and (new_x, new_y) not in visited
                ):
                    stack.append((new_x, new_y))

    return False


def generate_caves(dungeon, width, height, start_points):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for x, y in start_points:
        for _ in range(1000):  # Number of steps in each cave system
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy

            if 0 < new_x < width - 1 and 0 < new_y < height - 1:
                dungeon[new_y][new_x] = Tile.FLOOR
                x, y = new_x, new_y


def generate_starting_grid(width, height):
    dungeon = [[Tile.WALL for _ in range(width)] for _ in range(height)]
    for i in range(width):
        for j in range(height):
            if i == 0 or j == 0 or i == width - 1 or j == height - 1:
                dungeon[j][i] = Tile.PWALL

    return dungeon


def determine_room_count(width, height):
    return 6


def connnect_origins(dungeon, width, height, cavern_origins):
    all_connected = False
    while not all_connected:
        generate_caves(dungeon, width, height, cavern_origins)

        all_connected = True
        for i in range(len(cavern_origins)):
            for j in range(i + 1, len(cavern_origins)):
                if not are_points_connected(
                    dungeon, cavern_origins[i], cavern_origins[j]
                ):
                    all_connected = False
                    break
            if not all_connected:
                break

def generate_dungeon_grid(width, height):
    grid = generate_starting_grid(width, height)
    room_count = determine_room_count(width, height)
    origins = add_caverns(grid, width, height, room_count)
    connnect_origins(grid, width, height, origins)

    # Ensure all start_points are connected

    return grid
