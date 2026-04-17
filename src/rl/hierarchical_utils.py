import numpy as np

# ---------- GLOBAL AGENT ----------

GLOBAL_WAIT_THRESHOLDS = [1.0, 4.0, 10.0]   # 4 bins
GLOBAL_QUEUE_THRESHOLDS = [10, 30, 60]       # 4 bins

GLOBAL_MODES = {
    0: "normal",
    1: "congestion_priority",
    2: "recovery_mode",
}

NUM_GLOBAL_STATES = 4 * 4   # waiting bin x queue bin
NUM_GLOBAL_ACTIONS = 3      # 3 global modes

# ---------- LOCAL AGENT ----------

LOCAL_WAIT_THRESHOLDS = [0.5, 2.0, 5.0]      # 4 bins
LOCAL_QUEUE_THRESHOLDS = [2, 8, 15]          # 4 bins
DURATION_THRESHOLDS = [20, 30, 40]           # 4 bins

LOCAL_ACTION_TO_DELTA = {
    0: -5,
    1: 0,
    2: +5,
}

NUM_LOCAL_STATES = 4 * 4 * 4 * 3   # wait x queue x duration x global_mode
NUM_LOCAL_ACTIONS = 3

def _bin_index(value: float, thresholds: list[float]) -> int:
    for i, t in enumerate(thresholds):
        if value < t:
            return i
    return len(thresholds)

# ---------- GLOBAL STATE ----------

def get_global_state(avg_waiting: float, total_queue: int) -> int:
    wait_bin = _bin_index(avg_waiting, GLOBAL_WAIT_THRESHOLDS)
    queue_bin = _bin_index(total_queue, GLOBAL_QUEUE_THRESHOLDS)
    return wait_bin * 4 + queue_bin   # 0..15

def choose_global_action(Q: np.ndarray, state: int, epsilon: float) -> int:
    if np.random.rand() < epsilon:
        return np.random.randint(NUM_GLOBAL_ACTIONS)
    return int(np.argmax(Q[state]))

# ---------- LOCAL STATE ----------

def get_local_state(local_waiting: float, local_queue: int, current_duration: int, global_mode: int) -> int:
    wait_bin = _bin_index(local_waiting, LOCAL_WAIT_THRESHOLDS)
    queue_bin = _bin_index(local_queue, LOCAL_QUEUE_THRESHOLDS)
    duration_bin = _bin_index(current_duration, DURATION_THRESHOLDS)

    # 4*4*4*3 = 192 states
    return (((wait_bin * 4) + queue_bin) * 4 + duration_bin) * 3 + global_mode

def choose_local_action(Q: np.ndarray, state: int, epsilon: float) -> int:
    if np.random.rand() < epsilon:
        return np.random.randint(NUM_LOCAL_ACTIONS)
    return int(np.argmax(Q[state]))

def apply_local_action(current_duration: int, action: int, global_mode: int) -> int:
    # Base delta from local action
    delta = LOCAL_ACTION_TO_DELTA[action]

    # Global mode bias
    if global_mode == 1:          # congestion_priority
        delta += 2
    elif global_mode == 2:        # recovery_mode
        delta += 4

    new_duration = current_duration + delta
    return int(np.clip(new_duration, 10, 50))

# ---------- REWARDS ----------

def get_global_reward(prev_avg_waiting: float, curr_avg_waiting: float,
                      prev_total_queue: int, curr_total_queue: int) -> float:
    wait_improvement = prev_avg_waiting - curr_avg_waiting
    queue_improvement = prev_total_queue - curr_total_queue
    return 5.0 * wait_improvement + 1.5 * queue_improvement

def get_local_reward(prev_local_waiting: float, curr_local_waiting: float,
                     prev_local_queue: int, curr_local_queue: int,
                     action: int) -> float:
    wait_improvement = prev_local_waiting - curr_local_waiting
    queue_improvement = prev_local_queue - curr_local_queue
    action_penalty = 0.1 * abs(LOCAL_ACTION_TO_DELTA[action])
    return 4.0 * wait_improvement + 1.0 * queue_improvement - action_penalty