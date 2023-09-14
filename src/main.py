import services.events
import services.engine
import services.state

if __name__ == "__main__":
    # Initialize
    event_manager = services.events.EventManager()
    game_engine = services.engine.GameEngine()
    state_manager = services.state.StateManager()
    
    # Dependency injection
    event_manager.register_services(state_manager)
    game_engine.register_services(event_manager)

    # Start
    game_engine.start()
