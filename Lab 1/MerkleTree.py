import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.leaves = [self.hash_data(data) for data in data_list]
        self.tree = self.build_tree(self.leaves)

    def hash_data(self, data):
        """Hashes the given data using SHA-256."""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self, leaves):
        """Recursively builds the Merkle tree from the leaves up to the root."""
        tree = [leaves]
        while len(tree[-1]) > 1:
            level = []
            for i in range(0, len(tree[-1]), 2):
                left = tree[-1][i]
                right = tree[-1][i + 1] if i + 1 < len(tree[-1]) else left  # Duplicate if odd number of nodes
                level.append(self.hash_data(left + right))
            tree.append(level)
        return tree

    def get_root(self):
        """Returns the root hash of the Merkle Tree."""
        return self.tree[-1][0] if self.tree else None

    def print_tree(self):
        """Prints each level of the Merkle Tree."""
        for i, level in enumerate(self.tree):
            print(f"Level {i}: {level}")

# Example usage
data = ["a", "b", "c", "d"]
merkle_tree = MerkleTree(data)
merkle_tree.print_tree()
print("\nMerkle Root:", merkle_tree.get_root())
