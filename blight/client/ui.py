from aioconsole import ainput


class UiManager:
    def register_services(self, conn_manager):
        self.conn_manager = conn_manager

    async def run(self):
        while True:
            data = await ainput("You: ")
            if data:
                self.conn_manager.send_message(data)
