# Basic-Blockchain-in-python
This code is a basic implementation of how a block chain data structure works. 
The blockchain starts with a genesis block, created using predefined data.

When a new block is added:

The hash of the last block is retrieved.

A new hash is generated based on the new block's data and the previous hash.

The new block is appended to the chain.

Each block’s integrity can be verified using the hashes, ensuring data has not been tampered with.
