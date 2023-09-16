from server.events import EventManager


class GameManager:
    events: EventManager

    is_running = True

    def register_services(
        self,
        event_manager: EventManager,
    ):
        self.events = event_manager

    def handle_command(self):
        command_actions = {
            "examine": self.events.examine,
            "push": self.events.push,
            "take": self.events.take,
            "drop": self.events.drop,
            "go": self.events.go,
            "l": self.events.look_around,
            "x": self.events.examine_object,
            "i": self.events.show_inventory,
            "z": self.events.wait,
            "quit": self.events.quit,
        }

        while self.is_running:
            command = input("> ").lower().split()
            action = command_actions.get(command[0], self.events.unknown_command)
            params = command[1:] if len(command) > 1 else []

            action(*params)
