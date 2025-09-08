from src.crypto.sha256 import sha256_hex

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # led.value(1)
        content = "{}{}{}{}".format(self.index, self.timestamp, self.data, self.prev_hash)
        # led.value(0)
        return sha256_hex(content.encode())