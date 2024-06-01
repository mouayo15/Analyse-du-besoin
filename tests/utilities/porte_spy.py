class PorteSpy:
    def __init__(self):
        self.open_called = False
        self.close_called = False

    def open(self):
        self.open_called = True

    def close(self):
        self.close_called = True
