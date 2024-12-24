import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_info = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_info).hexdigest()


class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        # No need to pass difficulty here
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Mine the block with the set difficulty
        start_time = time.time()
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = self.mine_block(new_block)
        self.chain.append(new_block)
        end_time = time.time()
        return end_time - start_time

    def mine_block(self, block):
        target = "0" * self.difficulty
        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block.hash

    def print_chain(self):
        for block in self.chain:
            print(block)



def test_blockchain():
    # Try mining blocks with increasing difficulty levels
    for difficulty in range(3, 6):  # Testing difficulties 3, 4, and 5
        print(f"Testing blockchain with difficulty {difficulty}:\n")
        blockchain = Blockchain(difficulty)
        total_time = 0

        # Add several blocks to the blockchain and calculate time taken for each
        for i in range(1, 4):  # Mine 3 blocks
            block_data = f"Block {i} data"
            new_block = Block(i, blockchain.get_latest_block().hash, block_data)
            time_taken = blockchain.add_block(new_block)
            total_time += time_taken
        print(f"Total time taken for mining with difficulty {difficulty}: {total_time:.2f} seconds\n")
        blockchain.print_chain()

if __name__ == "__main__":
    test_blockchain()
