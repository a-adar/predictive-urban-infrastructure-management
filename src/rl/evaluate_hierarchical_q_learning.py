import traci
import numpy as np

from hierarchical_utils import (
    get_global_state,
    get_local_state,
    apply_local_action,
)

SUMO_CONFIG = "simulation/configs/chicago.sumocfg"

GLOBAL_CONTROL_INTERVAL = 150
LOCAL_CONTROL_INTERVAL = 60
USE_GUI = True

global_Q = np.load("results/rl/global_q_table.npy")
local_Q = np.load("results/rl/local_q_table.npy")

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

sumo_binary = "sumo-gui" if USE_GUI else "sumo"
traci.start([sumo_binary, "-c", SUMO_CONFIG])

step = 0
tls_ids = traci.trafficlight.getIDList()
tls_durations = {tls: 25 for tls in tls_ids}
global_mode = 0

while step < 3600:
    traci.simulationStep()
    step += 1

    if step % GLOBAL_CONTROL_INTERVAL == 0:
        avg_waiting, total_queue = get_global_metrics()
        global_state = get_global_state(avg_waiting, total_queue)
        global_mode = int(np.argmax(global_Q[global_state]))

        print(
            f"[GLOBAL] Step {step} | Avg waiting: {avg_waiting:.2f} | "
            f"Queue: {total_queue} | Mode: {global_mode}"
        )

    if step % LOCAL_CONTROL_INTERVAL == 0:
        for tls in tls_ids:
            local_waiting, local_queue = get_tls_metrics(tls)
            current_duration = tls_durations[tls]

            local_state = get_local_state(local_waiting, local_queue, current_duration, global_mode)
            local_action = int(np.argmax(local_Q[local_state]))

            new_duration = apply_local_action(current_duration, local_action, global_mode)
            traci.trafficlight.setPhaseDuration(tls, new_duration)
            tls_durations[tls] = new_duration

            print(
                f"[LOCAL] Step {step} | TLS: {tls} | "
                f"Wait: {local_waiting:.2f} | Queue: {local_queue} | "
                f"Action: {local_action} | Duration: {new_duration}"
            )

traci.close()