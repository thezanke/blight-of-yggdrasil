from math import sqrt
import random


WALL = "#"
FLOOR = "."

def find_densest_area(dungeon, width, height, subgrid_size=5):
    max_walls = 0
    dense_x, dense_y = 0, 0
    
    for x in range(1, width - subgrid_size):
        for y in range(1, height - subgrid_size):
            walls = sum(
                dungeon[y + dy][x + dx] == WALL
                for dy in range(subgrid_size)
                for dx in range(subgrid_size)
            )
            if walls > max_walls:
                max_walls = walls
                dense_x, dense_y = x, y
                
    return dense_x + subgrid_size // 2, dense_y + subgrid_size // 2

def hollow_organic_rooms(dungeon, width, height, room_count):
    start_points = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(room_count):
        if start_points:
            # Find the next densest area to start the new room
            x, y = find_densest_area(dungeon, width, height)
        else:
            # For the first room, start randomly
            x, y = random.randint(1, width-2), random.randint(1, height-2)
        
        start_points.append((x, y))
        
        for _ in range(width*height//10):  # Number of steps to hollow out the room
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy

            if 0 < new_x < width - 1 and 0 < new_y < height - 1:
                dungeon[new_y][new_x] = FLOOR
                x, y = new_x, new_y
                
    return start_points

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
                if dungeon[new_y][new_x] == FLOOR and (new_x, new_y) not in visited:
                    stack.append((new_x, new_y))

    return False


def generate_caves(dungeon, width, height, start_points):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for x, y in start_points:
        for _ in range(1000):  # Number of steps in each cave system
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy

            if 0 < new_x < width - 1 and 0 < new_y < height - 1:
                dungeon[new_y][new_x] = FLOOR
                x, y = new_x, new_y

def generate_dungeon(width, height):
    dungeon = [[WALL for _ in range(width)] for _ in range(height)]

    room_count = (width * height) // 400
    print(f"Generating {room_count} rooms...")
    start_points = hollow_organic_rooms(dungeon, width, height, room_count)

    # Ensure all start_points are connected
    all_connected = False
    while not all_connected:
        generate_caves(dungeon, width, height, start_points)
        
        all_connected = True
        for i in range(len(start_points)):
            for j in range(i+1, len(start_points)):
                if not are_points_connected(dungeon, start_points[i], start_points[j]):
                    all_connected = False
                    break
            if not all_connected:
                break

    return dungeon

