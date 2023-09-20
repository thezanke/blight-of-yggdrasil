import asyncio
from yggdrasil.logging import add_log_level_arg
from yggdrasil.server.events import EventManager
from yggdrasil.server.engine import GameManager
from yggdrasil.server.state import StateManager
from yggdrasil.server.net import ServerConnectionManager


def start_server(args):
    # Initialize
    event_manager = EventManager()
    game_manager = GameManager()
    state_manager = StateManager()
    conn_manager = ServerConnectionManager()

    # Dependency injection
    conn_manager.register_services(game_manager)
    event_manager.register_services(state_manager)
    game_manager.register_services(event_manager)

    # Start
    asyncio.run(conn_manager.run())


def attach_subparser(base):
    parser = base.add_parser("server")
    parser.set_defaults(func=start_server)
    add_log_level_arg(parser)

    return parser
