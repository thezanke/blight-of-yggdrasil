import threading


class StateManager:
    def __init__(self):
        self.data = "Initial Data"
        self.lock = threading.Lock()

    def update_data(self, new_data):
        with self.lock:
            self.data = new_data

    def read_data(self):
        with self.lock:
            return self.data
