import asyncio

from server.engine import GameManager


class ServerConnectionProtocol(asyncio.Protocol):
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager

    def connection_made(self, transport):
        self.connection_manager.connection_made(transport)

    def data_received(self, data):
        self.connection_manager.data_received(data)


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

        async with server:
            await server.serve_forever()

    def connection_made(self, transport):
        print(f"Connection from {transport.get_extra_info('peername')}")

    def data_received(self, data):
        print(f"Data received: {data.decode()}")
