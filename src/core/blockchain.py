import time
from .block import Block
from machine import Pin

led = Pin(25, Pin.OUT)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            led.value(1)
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
            led.value(0)
            time.sleep(0.1)
        return True

    def print_chain(self):
        for block in self.chain:
            print("-" * 40)
            print("Block:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Prev Hash:", block.prev_hash)
            print("Hash:", block.hash)