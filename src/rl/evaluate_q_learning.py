import traci
import numpy as np

from rl_utils import get_state, apply_action

SUMO_CONFIG = "simulation/configs/chicago.sumocfg"
CONTROL_INTERVAL = 30
USE_GUI = True

Q = np.load("results/rl/q_table.npy")

def collect_metrics():
    lanes = traci.lane.getIDList()
    waiting_times = [traci.lane.getWaitingTime(l) for l in lanes]
    queue_lengths = [traci.lane.getLastStepHaltingNumber(l) for l in lanes]

    avg_waiting = sum(waiting_times) / len(waiting_times) if waiting_times else 0.0
    total_queue = sum(queue_lengths) if queue_lengths else 0
    vehicle_count = traci.vehicle.getIDCount()

    return avg_waiting, total_queue, vehicle_count

sumo_binary = "sumo-gui" if USE_GUI else "sumo"
traci.start([sumo_binary, "-c", SUMO_CONFIG])

step = 0
current_duration = 25

while step < 3600:
    traci.simulationStep()
    step += 1

    if step % CONTROL_INTERVAL == 0:
        avg_waiting, total_queue, vehicle_count = collect_metrics()
        state = get_state(avg_waiting, total_queue, current_duration)

        action = int(np.argmax(Q[state]))
        current_duration = apply_action(current_duration, action)

        print(
            f"Step {step} | Avg waiting: {avg_waiting:.2f} | "
            f"Queue: {total_queue} | Vehicles: {vehicle_count} | "
            f"State: {state} | Action: {action} | Duration: {current_duration}"
        )

        for tls in traci.trafficlight.getIDList():
            traci.trafficlight.setPhaseDuration(tls, current_duration)

traci.close()