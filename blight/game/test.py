import blight.game as game

dungeon = game.generate_dungeon(120, 40)
player_starts = game.find_start_positions(dungeon, 10)
game.print_dungeon(dungeon, player_starts)
