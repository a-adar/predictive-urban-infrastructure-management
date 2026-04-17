import traci
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from hierarchical_utils import (
    NUM_GLOBAL_STATES,
    NUM_GLOBAL_ACTIONS,
    NUM_LOCAL_STATES,
    NUM_LOCAL_ACTIONS,
    get_global_state,
    choose_global_action,
    get_local_state,
    choose_local_action,
    apply_local_action,
    get_global_reward,
    get_local_reward,
)

SUMO_CONFIG = "simulation/configs/chicago.sumocfg"

GLOBAL_CONTROL_INTERVAL = 150
LOCAL_CONTROL_INTERVAL = 60
NUM_EPISODES = 20

ALPHA = 0.1
GAMMA = 0.95
EPSILON = 0.30
EPSILON_DECAY = 0.98
MIN_EPSILON = 0.05

def get_global_metrics():
    lanes = traci.lane.getIDList()
    waiting_times = [traci.lane.getWaitingTime(l) for l in lanes]
    queue_lengths = [traci.lane.getLastStepHaltingNumber(l) for l in lanes]

    avg_waiting = sum(waiting_times) / len(waiting_times) if waiting_times else 0.0
    total_queue = sum(queue_lengths) if queue_lengths else 0
    return avg_waiting, total_queue

def get_tls_metrics(tls_id):
    lanes = list(set(traci.trafficlight.getControlledLanes(tls_id)))
    waiting_times = [traci.lane.getWaitingTime(l) for l in lanes if l in traci.lane.getIDList()]
    queue_lengths = [traci.lane.getLastStepHaltingNumber(l) for l in lanes if l in traci.lane.getIDList()]

    local_waiting = sum(waiting_times) / len(waiting_times) if waiting_times else 0.0
    local_queue = sum(queue_lengths) if queue_lengths else 0
    return local_waiting, local_queue

global_Q = np.zeros((NUM_GLOBAL_STATES, NUM_GLOBAL_ACTIONS))
local_Q = np.zeros((NUM_LOCAL_STATES, NUM_LOCAL_ACTIONS))

episode_rewards = []

for episode in range(NUM_EPISODES):
    traci.start(["sumo", "-c", SUMO_CONFIG, "--no-step-log", "true"])

    step = 0
    total_reward = 0.0

    tls_ids = traci.trafficlight.getIDList()
    tls_durations = {tls: 25 for tls in tls_ids}

    global_avg_waiting, global_total_queue = get_global_metrics()
    global_state = get_global_state(global_avg_waiting, global_total_queue)
    global_mode = choose_global_action(global_Q, global_state, EPSILON)

    prev_global_state = global_state
    prev_global_avg_waiting = global_avg_waiting
    prev_global_total_queue = global_total_queue
    prev_global_action = global_mode

    # Store local previous state per junction
    local_prev = {}

    while step < 1200:
        traci.simulationStep()
        step += 1

        # ----- Global agent -----
        if step % GLOBAL_CONTROL_INTERVAL == 0:
            global_avg_waiting, global_total_queue = get_global_metrics()
            global_state = get_global_state(global_avg_waiting, global_total_queue)

            reward_g = get_global_reward(
                prev_global_avg_waiting, global_avg_waiting,
                prev_global_total_queue, global_total_queue
            )
            total_reward += reward_g

            global_Q[prev_global_state, prev_global_action] = global_Q[prev_global_state, prev_global_action] + ALPHA * (
                reward_g + GAMMA * np.max(global_Q[global_state]) - global_Q[prev_global_state, prev_global_action]
            )

            global_mode = choose_global_action(global_Q, global_state, EPSILON)

            prev_global_state = global_state
            prev_global_avg_waiting = global_avg_waiting
            prev_global_total_queue = global_total_queue
            prev_global_action = global_mode

        # ----- Local agent for each junction -----
        if step % LOCAL_CONTROL_INTERVAL == 0:
            for tls in tls_ids:
                local_waiting, local_queue = get_tls_metrics(tls)
                current_duration = tls_durations[tls]

                local_state = get_local_state(local_waiting, local_queue, current_duration, global_mode)

                if tls in local_prev:
                    prev_state, prev_wait, prev_queue, prev_action = local_prev[tls]

                    reward_l = get_local_reward(prev_wait, local_waiting, prev_queue, local_queue, prev_action)
                    total_reward += reward_l

                    local_Q[prev_state, prev_action] = local_Q[prev_state, prev_action] + ALPHA * (
                        reward_l + GAMMA * np.max(local_Q[local_state]) - local_Q[prev_state, prev_action]
                    )

                local_action = choose_local_action(local_Q, local_state, EPSILON)
                new_duration = apply_local_action(current_duration, local_action, global_mode)

                traci.trafficlight.setPhaseDuration(tls, new_duration)
                tls_durations[tls] = new_duration

                local_prev[tls] = (local_state, local_waiting, local_queue, local_action)

    traci.close()
    episode_rewards.append(total_reward)

    print(f"Episode {episode+1}/{NUM_EPISODES} | Total reward: {total_reward:.2f} | Epsilon: {EPSILON:.3f}")

    EPSILON = max(MIN_EPSILON, EPSILON * EPSILON_DECAY)

Path("results/rl").mkdir(parents=True, exist_ok=True)

np.save("results/rl/global_q_table.npy", global_Q)
np.save("results/rl/local_q_table.npy", local_Q)

reward_df = pd.DataFrame({
    "episode": list(range(1, NUM_EPISODES + 1)),
    "total_reward": episode_rewards
})
reward_df.to_csv("results/rl/hierarchical_training_rewards.csv", index=False)

plt.figure(figsize=(8, 5))
plt.plot(reward_df["episode"], reward_df["total_reward"], marker="o")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Hierarchical Q-Learning Training Reward by Episode")
plt.tight_layout()
plt.savefig("results/rl/hierarchical_training_rewards.png")
plt.show()

print("Saved hierarchical RL outputs:")
print("- results/rl/global_q_table.npy")
print("- results/rl/local_q_table.npy")
print("- results/rl/hierarchical_training_rewards.csv")
print("- results/rl/hierarchical_training_rewards.png")