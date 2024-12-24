# Mini Social Network DApp

A decentralized "Mini Social Network" implemented in Solidity, allowing users to publish, view, and count posts on the Ethereum blockchain. This smart contract application is a basic decentralized social network where users can post messages, view posts, and track the total number of posts, deployed using the Remix IDE and a test Ethereum network.

![DApp](https://kingslanduniversity.com/wp-content/uploads/2019/06/dapps-1024x512.jpg)

## Features

1. **Publish a Post**: Allows users to publish messages that are stored on the blockchain.
2. **Retrieve a Post**: Users can retrieve a specific post and see the message and author address.
3. **Count Total Posts**: Keeps track of the total number of posts in the network.

## Project Structure

- **MiniSocial.sol**: Solidity smart contract file containing the contract definition and functions.

## Smart Contract Functions

1. **publishPost**: Allows a user to publish a new post.
2. **getPost**: Retrieves a specific post by index.
3. **getTotalPosts**: Returns the total number of posts published.

## Setup and Deployment

1. **Remix IDE**:
   - Open [Remix IDE](https://remix.ethereum.org/).
   - Create a new file named `MiniSocial.sol` and paste the contract code.

2. **Compile the Contract**:
   - In Remix, go to the "Solidity Compiler" tab.
   - Compile `MiniSocial.sol`.

3. **Deploy the Contract**:
   - Go to the "Deploy & Run Transactions" tab.
   - Deploy the `MiniSocial` contract.

---

This repository serves as a simple introduction to creating decentralized applications (DApps) with Solidity and is designed for educational purposes.
