Compare and contrast the technical capabiliƟes of each.
Ans. Comparison of Ethereum, Hyperledger Fabric, and R3 Corda
Ethereum, Hyperledger Fabric, and R3 Corda represent three disƟnct blockchain types—public,
private, and consorƟum—each with unique technical capabiliƟes.
1. Ethereum
 A public blockchain, uses Proof-of-Stake (PoS) for consensus, offering 15–30 TPS (scalable via
Layer 2 soluƟons). It supports smart contracts (Solidity/Vyper) and naƟve tokens (ETH + ERC20), making it ideal for DeFi, NFTs, and dApps. Its key strength is decentralizaƟon, though it
sacrifices speed and privacy.
2. Hyperledger Fabric
 A private blockchain, employs a pluggable consensus (e.g., RaŌ) and achieves 1,000–10,000
TPS. It supports smart contracts in Go/Java/JS but lacks naƟve tokens. Designed for
enterprises, it ensures privacy via channels, making it suitable for supply chain and
healthcare.
3. R3 Corda
 A consorƟum blockchain, uses a notary-based consensus and processes 100–1,000 TPS. It
supports smart contracts (Kotlin/Java) and opƟonal tokenizaƟon. OpƟmized for financial and
legal agreements, it enforces need-to-know data privacy and integrates legal prose.
Que 3. Which plaƞorm would you choose for:
 A decentralized app?
 A supply chain network among known partners?
 An inter-bank financial applicaƟon?
JusƟfy your choice based on technical points.
Ans.
1. Decentralized App (DApp)
Choice: Ethereum
 Open Permissionless Model: Allows anyone to parƟcipate (criƟcal for DApps).
 Smart Contract Support: Solidity/Vyper enable complex logic (DeFi, NFTs).
 TokenizaƟon: NaƟve ETH + ERC-20 standard for token economies.
 L2 Scaling: Rollups (e.g., Arbitrum) miƟgate low base-layer TPS (~15–30).
 Network Effects: Largest developer ecosystem and interoperability standards.
2. Supply Chain Network Among Known Partners
Choice: Hyperledger Fabric
 Permissioned Model: Only authorized partners join (enterprise requirement).
 High Throughput: 1,000–10,000 TPS handles supply chain data volume.
 Channels: Isolate sensiƟve data (e.g., supplier contracts).
 No NaƟve Token: Avoids regulatory complexity for enterprise use.
 Pluggable Consensus: Tailor consensus (e.g., RaŌ) to partner needs.
3. Inter-Bank Financial ApplicaƟon
Choice: R3 Corda
 ConsorƟum Model: Banks retain control (vs. public chains).
 Notary-Based Consensus: DeterminisƟc finality (no forks, criƟcal for finance).
 Privacy: Only parƟes to a transacƟon see data (vs. Fabric’s channel overhead).
 Legal Prose IntegraƟon: Enforce real-world contracts on-chain.
 Tokens SDK: OpƟonal asset tokenizaƟon (e.g., CBDCs, securies).
