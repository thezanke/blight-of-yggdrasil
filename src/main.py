import server.events
import server.engine
import server.state

if __name__ == "__main__":
    # Initialize
    event_manager = server.events.EventManager()
    game_engine = server.engine.GameEngine()
    state_manager = server.state.StateManager()

    # Dependency injection
    event_manager.register_services(state_manager)
    game_engine.register_services(event_manager)

    # Start
    game_engine.start()
