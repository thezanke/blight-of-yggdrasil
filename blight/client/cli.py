import asyncio
import curses
from blight.logging import add_log_level_arg
from .net import ClientConnectionManager
from .state import StateManager
from .ui import InterfaceManager


def run_all(args):
    game_state = StateManager()
    conn = ClientConnectionManager(game_state)
    ui = InterfaceManager(game_state, conn.send_message)
    
    curses.wrapper(ui.run)


def start_play(args):
    run_all(args)


def attach_subparser(base):
    parser = base.add_parser("client")
    parser.set_defaults(func=start_play)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=12529)
    add_log_level_arg(parser)

    return parser
