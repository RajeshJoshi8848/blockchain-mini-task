import hashlib
import time

class Block:
    def __init__(self, index, data):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.nonce = 0
        self.hash = ''

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + self.timestamp + str(self.data) + str(self.nonce)).encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"Mining block with difficulty {difficulty}...")
        start_time = time.time()
        prefix = '0' * difficulty
        attempts = 0
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(prefix):
                break
            self.nonce += 1
            attempts += 1
        end_time = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce found: {self.nonce}")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {round(end_time - start_time, 2)} seconds")

block = Block(1, "Mining Simulation Block")
block.mine_block(difficulty=4)
