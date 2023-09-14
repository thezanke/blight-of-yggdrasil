class PlayerState:
    name: str = "Player"
    health: int = 100
    mana: int = 100
    stamina: int = 100
    gold: int = 0
    inventory: list = []
    location: str = "start"


class StateManager:
    player = PlayerState()

    game_map = {
        "start": {"n": "forest", "s": "beach"},
        "forest": {"s": "start"},
        "beach": {"n": "start"},
    }
