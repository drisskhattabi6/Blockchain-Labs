#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

// Define the structure for a Merkle Tree node
typedef struct Node {
    unsigned char hash[SHA256_DIGEST_LENGTH];  // Hash (SHA-256)
    struct Node* left;  // Pointer to the left child
    struct Node* right; // Pointer to the right child
} Node;

// Function to print a hash in hexadecimal format
void printHash(unsigned char hash[SHA256_DIGEST_LENGTH]) {
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");
}

// Function to compute the SHA-256 hash of input data
void computeHash(const char* data, unsigned char output[SHA256_DIGEST_LENGTH]) {
    SHA256((unsigned char*)data, strlen(data), output);
}

// Function to create a new node with a given hash
Node* createNode(const char* data) {
    Node* node = (Node*)malloc(sizeof(Node));
    if (data != NULL) {
        computeHash(data, node->hash);
    }
    node->left = node->right = NULL;
    return node;
}

// Function to create a parent node by combining the hashes of two children
Node* createParentNode(Node* left, Node* right) {
    Node* parent = (Node*)malloc(sizeof(Node));
    
    // Concatenate the left and right hashes to form the parent node's data
    unsigned char combined[2 * SHA256_DIGEST_LENGTH];
    memcpy(combined, left->hash, SHA256_DIGEST_LENGTH);
    memcpy(combined + SHA256_DIGEST_LENGTH, right->hash, SHA256_DIGEST_LENGTH);
    
    // Compute the parent node's hash
    SHA256(combined, 2 * SHA256_DIGEST_LENGTH, parent->hash);
    parent->left = left;
    parent->right = right;
    
    return parent;
}

// Function to build a Merkle tree from an array of leaf nodes
Node* buildMerkleTree(Node* nodes[], int count) {
    while (count > 1) {
        int newCount = (count + 1) / 2;
        for (int i = 0; i < newCount; i++) {
            if (2 * i + 1 < count) {
                nodes[i] = createParentNode(nodes[2 * i], nodes[2 * i + 1]);
            } else {
                // Handle odd number of nodes by duplicating the last one
                nodes[i] = createParentNode(nodes[2 * i], nodes[2 * i]);
            }
        }
        count = newCount;
    }
    return nodes[0]; // Root node
}

// Main function to demonstrate the Merkle Tree
int main() {
    // Array of data (leaf nodes)
    const char* data[] = {"block1", "block2", "block3", "block4"};
    int dataSize = sizeof(data) / sizeof(data[0]);
    
    // Create leaf nodes
    Node* nodes[dataSize];
    for (int i = 0; i < dataSize; i++) {
        nodes[i] = createNode(data[i]);
        printf("Leaf %d hash: ", i);
        printHash(nodes[i]->hash);
    }
    
    // Build the Merkle Tree and get the root
    Node* root = buildMerkleTree(nodes, dataSize);
    
    // Print the root hash
    printf("Merkle Root Hash: ");
    printHash(root->hash);
    
    return 0;
}

// sudo apt-get install libssl-dev
// gcc merkle_tree.c -o merkle_tree -lssl -lcrypto
// ./merkle_tree
