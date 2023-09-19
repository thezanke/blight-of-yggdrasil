import asyncio

from yggdrasil.server.engine import GameManager


class ServerConnectionProtocol(asyncio.Protocol):
    transport: asyncio.Transport = None

    def __init__(self, connection_manager):
        self.connection_manager = connection_manager

    def connection_made(self, transport):
        self.transport = transport
        self.connection_manager.connection_made(transport)

    def data_received(self, data):
        self.connection_manager.data_received(data)

    def connection_lost(self, exc):
        self.connection_manager.connection_lost(self.transport, exc)


class ServerConnectionManager:
    def register_services(self, game_manager: GameManager):
        self.game_manager = game_manager

    async def run(self, hostname="127.0.0.1", port=12529):
        loop = asyncio.get_running_loop()

        server = await loop.create_server(
            lambda: ServerConnectionProtocol(self),
            hostname,
            port,
        )

        print(f'message="server started", hostname="{hostname}", port={port}')

        async with server:
            await server.serve_forever()

    def data_received(self, data):
        print(f'message="data received", data="{data.decode()}"')

    def connection_made(self, transport):
        print(
            f'message="connection", peername="{transport.get_extra_info("peername")}"'
        )

    def connection_lost(self, transport, exc):
        print(
            f'message="connection closed", peername="{transport.get_extra_info("peername")}", exception="{exc}"'
        )
