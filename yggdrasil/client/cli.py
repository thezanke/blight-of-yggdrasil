import asyncio
from yggdrasil.client.net import ClientConnectionManager
from yggdrasil.client.ui import UiManager


async def run_all(args):
    conn_manager = ClientConnectionManager()
    ui_manager = UiManager()

    # Dependency injection
    ui_manager.register_services(conn_manager)

    await asyncio.gather(conn_manager.run(args.host, args.port), ui_manager.run())


def start_play(args):
    asyncio.run(run_all(args))


def attach_subparser(base):
    parser = base.add_parser("client")
    parser.set_defaults(func=start_play)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=12529)

    return parser