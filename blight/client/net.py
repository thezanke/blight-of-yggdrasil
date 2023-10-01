import asyncio


class ClientConnectionManager:
    def __init__(self, game_state):
        self.transport = None
        self.game_state = game_state

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


# import time

# def network_loop(game_state):
#     counter = 0
#     while True:
#         time.sleep(2)  # Simulating network delay
#         counter += 1
#         new_data = f"Updated Data {counter}"
#         game_state.update_data(new_data)
