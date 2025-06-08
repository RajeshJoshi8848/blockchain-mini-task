Blockchain Basics
Q1: Define blockchain in your own words (100–150 words).
Blockchain is a decentralized digital ledger that records data in a secure, transparent, and immutable way. It consists of a chain of blocks, where each block holds a group of transactions, a timestamp, and a unique hash value. Each block is linked to the previous one using its hash, creating a continuous and tamper-resistant chain. Unlike traditional centralized databases, blockchain operates on a peer-to-peer network, eliminating the need for a central authority. This distributed nature ensures that data is replicated across all nodes, making it highly secure and resistant to manipulation. Once data is added to a block and confirmed, it becomes permanent and cannot be altered. Blockchain technology is the foundation of cryptocurrencies like Bitcoin and Ethereum, but it also has many other applications across industries due to its ability to maintain trust, transparency, and data integrity.

Q2: List 2 real-life use cases.
Supply Chain Management
Blockchain helps track the movement of goods across the supply chain. It ensures transparency by recording each step from the manufacturer to the consumer, making it easier to detect fraud, reduce errors, and verify product authenticity.

Digital Identity Verification
Blockchain allows individuals to store and manage their digital identities securely. It can be used for applications such as online voting, passport verification, and accessing services without sharing unnecessary personal data.


Block Anatomy

Q3: Draw a block showing: data, previous hash, timestamp, nonce, and Merkle root.
(Note: Since diagrams aren't allowed or desired, the structure is described below.)

A blockchain block consists of the following key components:

Data: Stores transaction details (e.g., sender, receiver, amount).

Previous Hash: The hash of the preceding block, linking the blocks.

Timestamp: The exact date and time when the block was created.

Nonce: A number used once, which miners adjust to find a valid block hash.

Merkle Root: A single hash representing all transactions in the block, used for verifying data integrity efficiently.

Q4: Briefly explain with an example how the Merkle root helps verify data integrity.
The Merkle root is the topmost hash in a Merkle tree, which is constructed by hashing pairs of transaction data recursively until one final hash remains. This root summarizes all transactions in a block. If even a single transaction is changed, the corresponding hash changes, causing a chain reaction up the tree and altering the Merkle root. For example, in a block containing four transactions (T1, T2, T3, T4), their hashes are combined into pairs and then hashed again until one root remains. If T2 is modified, the hash of T2 changes, which affects the Merkle root. Thus, Merkle roots help quickly verify if the block's data is unchanged without needing to check every transaction individually.

Consensus Conceptualization
Q5: What is Proof of Work and why does it require energy?
Proof of Work (PoW) is a consensus mechanism where network participants, known as miners, compete to solve complex mathematical puzzles to validate and add new blocks to the blockchain. The process involves repeatedly trying different values (nonces) until a hash meeting a specific difficulty is found. This requires significant computational power, leading to high energy consumption. The energy-intensive nature of PoW makes it difficult for any single entity to control the network and helps secure the blockchain against attacks such as double spending.

Q6: What is Proof of Stake and how does it differ?
Proof of Stake (PoS) is an energy-efficient alternative to Proof of Work. In PoS, validators are chosen to create new blocks based on the amount of cryptocurrency they "stake" or lock in the network. The higher the stake, the greater the chance of being selected. Unlike PoW, PoS does not require solving complex puzzles, thus consuming much less energy. It relies on economic incentives and penalties to maintain security and encourage honest behavior among validators.

Q7: What is Delegated Proof of Stake and how are validators selected?
Delegated Proof of Stake (DPoS) is a variation of PoS where token holders vote for a limited number of delegates (validators) who are responsible for validating transactions and producing blocks. The selection is based on democratic voting, where users choose trusted representatives instead of participating directly in block validation. If a delegate acts dishonestly, they can be replaced by community votes. DPoS increases transaction speed and network efficiency while maintaining decentralization through community governance.
