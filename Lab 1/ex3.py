import hashlib
import time
import random

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Used for PoW
        self.hash = self.calculate_hash()

    # Function to calculate the block's hash
    def calculate_hash(self):
        block_info = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_info).hexdigest()

    def __str__(self):
        return f"Block {self.index} [Hash: {self.hash}, Data: {self.data}, Previous Hash: {self.previous_hash}]"



class PoW_Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    # Create the first block (genesis block)
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    # Get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Add a new block to the chain
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = self.mine_block(new_block)
        self.chain.append(new_block)

    # Proof of Work (PoW) method: find the hash with the required number of leading zeros
    def mine_block(self, block):
        target = "0" * self.difficulty
        start_time = time.time()
        print(f"Mining block with difficulty {self.difficulty}...")

        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.calculate_hash()

        end_time = time.time()
        print(f"Block mined: {block.hash}")
        print(f"Time taken for PoW: {end_time - start_time} seconds\n")
        return block.hash


class Validator:
    def __init__(self, name, stake):
        self.name = name
        self.stake = stake  # Amount of coins held by validator

class PoS_Blockchain:
    def __init__(self, validators):
        self.chain = [self.create_genesis_block()]
        self.validators = validators  # List of validators (with stakes)

    # Create the first block (genesis block)
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    # Get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Select a validator based on stake
    def select_validator(self):
        total_stake = sum([validator.stake for validator in self.validators])
        rand = random.uniform(0, total_stake)
        current = 0
        for validator in self.validators:
            current += validator.stake
            if current > rand:
                return validator.name

    # Add a new block to the chain
    def add_block(self, new_block):
        start_time = time.time()
        selected_validator = self.select_validator()
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()

        end_time = time.time()
        print(f"Block validated by {selected_validator} with PoS")
        print(f"Time taken for PoS: {end_time - start_time} seconds\n")
        self.chain.append(new_block)


def compare_pow_and_pos():
    # Testing Proof of Work (PoW) with difficulty 4
    print("=== Proof of Work (PoW) ===")
    pow_blockchain = PoW_Blockchain(difficulty=4)
    pow_blockchain.add_block(Block(1, pow_blockchain.get_latest_block().hash, "PoW Block 1"))
    pow_blockchain.add_block(Block(2, pow_blockchain.get_latest_block().hash, "PoW Block 2"))

    # Testing Proof of Stake (PoS)
    print("\n=== Proof of Stake (PoS) ===")
    validators = [
        Validator("Alice", stake=10),
        Validator("Bob", stake=20),
        Validator("Charlie", stake=30)
    ]
    pos_blockchain = PoS_Blockchain(validators=validators)
    pos_blockchain.add_block(Block(1, pos_blockchain.get_latest_block().hash, "PoS Block 1"))
    pos_blockchain.add_block(Block(2, pos_blockchain.get_latest_block().hash, "PoS Block 2"))

if __name__ == "__main__":
    compare_pow_and_pos()
