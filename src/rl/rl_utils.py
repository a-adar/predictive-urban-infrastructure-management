import numpy as np

# Tuned for live simulation metrics, not tripinfo averages
WAIT_THRESHOLDS = [0.5, 2.0, 5.0]      # 4 bins
QUEUE_THRESHOLDS = [5, 15, 30]         # 4 bins
DURATION_THRESHOLDS = [20, 30, 40]     # 4 bins

# Actions are relative changes, not fixed durations
ACTION_TO_DELTA = {
    0: -10,
    1: -5,
    2: 0,
    3: 5,
    4: 10,
}

NUM_STATES = 64   # 4 wait bins * 4 queue bins * 4 duration bins
NUM_ACTIONS = 5

def _bin_index(value: float, thresholds: list[float]) -> int:
    for i, t in enumerate(thresholds):
        if value < t:
            return i
    return len(thresholds)

def get_state(avg_waiting: float, total_queue: int, current_duration: int) -> int:
    wait_bin = _bin_index(avg_waiting, WAIT_THRESHOLDS)         # 0..3
    queue_bin = _bin_index(total_queue, QUEUE_THRESHOLDS)       # 0..3
    duration_bin = _bin_index(current_duration, DURATION_THRESHOLDS)  # 0..3
    return wait_bin * 16 + queue_bin * 4 + duration_bin         # 0..63

def choose_action(Q: np.ndarray, state: int, epsilon: float) -> int:
    if np.random.rand() < epsilon:
        return np.random.randint(NUM_ACTIONS)
    return int(np.argmax(Q[state]))

def apply_action(current_duration: int, action: int) -> int:
    new_duration = current_duration + ACTION_TO_DELTA[action]
    return int(np.clip(new_duration, 10, 45))

def get_reward(prev_waiting: float, curr_waiting: float,
               prev_queue: int, curr_queue: int,
               action: int) -> float:
    # Reward improvements in waiting and queue, penalise abrupt changes a little
    wait_improvement = prev_waiting - curr_waiting
    queue_improvement = prev_queue - curr_queue
    action_penalty = 0.05 * abs(ACTION_TO_DELTA[action])

    return 5.0 * wait_improvement + 1.0 * queue_improvement - action_penalty