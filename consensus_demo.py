import random

# -----------------------------
# Proof of Work Simulation
# -----------------------------
miner_A = {"name": "Miner_A", "power": random.randint(1, 100)}
miner_B = {"name": "Miner_B", "power": random.randint(1, 100)}

pow_winner = miner_A if miner_A["power"] > miner_B["power"] else miner_B
print("\nProof of Work (PoW):")
print(f"{miner_A['name']} Power: {miner_A['power']}")
print(f"{miner_B['name']} Power: {miner_B['power']}")
print(f"Selected: {pow_winner['name']} (highest computational power)\n")

# -----------------------------
# Proof of Stake Simulation
# -----------------------------
staker_A = {"name": "Staker_A", "stake": random.randint(100, 1000)}
staker_B = {"name": "Staker_B", "stake": random.randint(100, 1000)}

pos_winner = staker_A if staker_A["stake"] > staker_B["stake"] else staker_B
print("Proof of Stake (PoS):")
print(f"{staker_A['name']} Stake: {staker_A['stake']}")
print(f"{staker_B['name']} Stake: {staker_B['stake']}")
print(f"Selected: {pos_winner['name']} (highest stake)\n")

# -----------------------------
# Delegated Proof of Stake Simulation
# -----------------------------
delegates = ["Delegate_A", "Delegate_B", "Delegate_C"]
votes = {
    "Voter1": random.choice(delegates),
    "Voter2": random.choice(delegates),
    "Voter3": random.choice(delegates),
}

vote_count = {}
for vote in votes.values():
    vote_count[vote] = vote_count.get(vote, 0) + 1

dpos_winner = max(vote_count, key=vote_count.get)

print("Delegated Proof of Stake (DPoS):")
print("Votes:", votes)
print("Vote Count:", vote_count)
print(f"Selected: {dpos_winner} (most voted delegate)\n")
