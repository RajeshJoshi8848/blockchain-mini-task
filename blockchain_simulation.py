import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + self.timestamp + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Create 3 blocks
block1 = Block(1, time.ctime(), "First Block Data", "0")
block2 = Block(2, time.ctime(), "Second Block Data", block1.hash)
block3 = Block(3, time.ctime(), "Third Block Data", block2.hash)

# Print blocks
for block in [block1, block2, block3]:
    print(f"\nBlock {block.index}")
    print(f"Data: {block.data}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")

# Challenge: Change data of block1 and recalculate hash
print("\nTampering with Block 1 data...\n")
block1.data = "Hacked Data"
block1.hash = block1.calculate_hash()

# Re-check chain integrity
print(f"Block 1 new hash: {block1.hash}")
print(f"Block 2 still points to: {block2.previous_hash}")
print("Observation: Block 2 and 3 are now invalid unless rehashed.")
