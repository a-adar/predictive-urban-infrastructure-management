import traci
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from rl_utils import (
    NUM_STATES,
    NUM_ACTIONS,
    get_state,
    choose_action,
    apply_action,
    get_reward,
)

# Train on medium first
SUMO_CONFIG = "simulation/configs/chicago.sumocfg"
CONTROL_INTERVAL = 30
NUM_EPISODES = 150

ALPHA = 0.1
GAMMA = 0.95
EPSILON = 0.30
EPSILON_DECAY = 0.98
MIN_EPSILON = 0.05

def collect_metrics():
    lanes = traci.lane.getIDList()
    waiting_times = [traci.lane.getWaitingTime(l) for l in lanes]
    queue_lengths = [traci.lane.getLastStepHaltingNumber(l) for l in lanes]

    avg_waiting = sum(waiting_times) / len(waiting_times) if waiting_times else 0.0
    total_queue = sum(queue_lengths) if queue_lengths else 0
    vehicle_count = traci.vehicle.getIDCount()

    return avg_waiting, total_queue, vehicle_count

Q = np.zeros((NUM_STATES, NUM_ACTIONS))
episode_rewards = []

for episode in range(NUM_EPISODES):
    traci.start(["sumo", "-c", SUMO_CONFIG, "--no-step-log", "true"])

    step = 0
    total_reward = 0.0
    current_duration = 25

    # Warm-up
    traci.simulationStep()
    step += 1

    avg_waiting, total_queue, vehicle_count = collect_metrics()
    state = get_state(avg_waiting, total_queue, current_duration)

    # Initial action
    action = choose_action(Q, state, EPSILON)
    current_duration = apply_action(current_duration, action)

    for tls in traci.trafficlight.getIDList():
        traci.trafficlight.setPhaseDuration(tls, current_duration)

    prev_state = state
    prev_action = action
    prev_waiting = avg_waiting
    prev_queue = total_queue

    while step < 3600:
        traci.simulationStep()
        step += 1

        if step % CONTROL_INTERVAL == 0:
            avg_waiting, total_queue, vehicle_count = collect_metrics()
            state = get_state(avg_waiting, total_queue, current_duration)

            reward = get_reward(
                prev_waiting, avg_waiting,
                prev_queue, total_queue,
                prev_action
            )
            total_reward += reward

            Q[prev_state, prev_action] = Q[prev_state, prev_action] + ALPHA * (
                reward + GAMMA * np.max(Q[state]) - Q[prev_state, prev_action]
            )

            action = choose_action(Q, state, EPSILON)
            current_duration = apply_action(current_duration, action)

            for tls in traci.trafficlight.getIDList():
                traci.trafficlight.setPhaseDuration(tls, current_duration)

            prev_state = state
            prev_action = action
            prev_waiting = avg_waiting
            prev_queue = total_queue

    traci.close()
    episode_rewards.append(total_reward)

    print(
        f"Episode {episode + 1}/{NUM_EPISODES} | "
        f"Total reward: {total_reward:.2f} | "
        f"Epsilon: {EPSILON:.3f}"
    )

    EPSILON = max(MIN_EPSILON, EPSILON * EPSILON_DECAY)

Path("results/rl").mkdir(parents=True, exist_ok=True)

np.save("results/rl/q_table.npy", Q)

reward_df = pd.DataFrame({
    "episode": list(range(1, NUM_EPISODES + 1)),
    "total_reward": episode_rewards
})
reward_df.to_csv("results/rl/training_rewards.csv", index=False)

plt.figure(figsize=(8, 5))
plt.plot(reward_df["episode"], reward_df["total_reward"], marker="o")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Q-Learning Training Reward by Episode")
plt.tight_layout()
plt.savefig("results/rl/training_rewards.png")
plt.show()

print("Saved:")
print("- results/rl/q_table.npy")
print("- results/rl/training_rewards.csv")
print("- results/rl/training_rewards.png")