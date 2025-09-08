from src.core.blockchain import Blockchain
from machine import Pin

led = Pin(25, Pin.OUT)  # Assuming an LED is connected to GPIO2

# Initialize the blockchain
bc = Blockchain()

led.value(0)  # Turn off LED initially
led.value(1)  # Turn on LED to indicate startup

print("MiniChain Running On RP2040")
print("Commands: add <data> | show | check")

led.value(0)  # Turn off LED after startup

while True:
    cmd = input(">> ").strip()
    if cmd.startswith("add "):
        data = cmd[4:]
        bc.add_block(data)
        print("Block added!")
    elif cmd == "show":
        bc.print_chain()
    elif cmd == "check":
        print("Chain valid" if bc.is_chain_valid() else "Chain INVALID!")
    else:
        print("Unknown command!")
