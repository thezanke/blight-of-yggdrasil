import asyncio

class ClientConnectionManager:
    def __init__(self):
        self.transport = None

    async def run(self, hostname="127.0.0.1", port=12529):
        loop = asyncio.get_running_loop()
        self.transport, _ = await loop.create_connection(
            asyncio.Protocol,
            hostname,
            port,
        )

    def send_message(self, message):
        if self.transport:
            self.transport.write(message.encode())