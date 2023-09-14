from services.state import StateManager


class EventManager:
    state: StateManager

    def register_services(self, state_manager: StateManager):
        self.state = state_manager

    def examine(self):
        print("You examine the area.")

    def push(self):
        print("You push the object.")

    def take(self):
        print("You take the item.")
        self.state.inventory.append("item")

    def drop(self):
        print("You drop the item.")
        self.state.inventory.remove("item")

    def go(self, direction):
        new_location = self.state.game_map.get(self.state.player.location, {}).get(direction)

        if new_location:
            print(f"You go {direction} to {new_location}.")
            return new_location
        else:
            print(f"You can't go {direction}.")
            return self.state.player.location

    def look_around(self):
        print("You look around.")

    def examine_object(self):
        print("You examine the object closely.")

    def show_inventory(self):
        print(f"Inventory: {self.state.player.inventory}")

    def wait(self):
        print("You wait.")

    def unknown_command(self):
        print("I don't understand that command.")

    def quit(self):
        print("You quit the game.")
