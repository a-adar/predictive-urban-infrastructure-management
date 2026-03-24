import traci
import pandas as pd
import joblib

SUMO_CONFIG = "simulation/configs/chicago.sumocfg"
model = joblib.load("results/model.pkl")

traci.start(["sumo-gui", "-c", SUMO_CONFIG])

step = 0
CONTROL_INTERVAL = 100
current_mode = "normal"

while step < 3600:
    traci.simulationStep()

    lanes = traci.lane.getIDList()

    waiting_times = []
    for lane in lanes:
        wt = traci.lane.getWaitingTime(lane)
        waiting_times.append(wt)

    if len(waiting_times) > 0:
        avg_waiting = sum(waiting_times) / len(waiting_times)
    else:
        avg_waiting = 0

    vehicle_count = traci.vehicle.getIDCount()

    if step % CONTROL_INTERVAL == 0:
        route_length_proxy = 100
        duration_proxy = avg_waiting
        scenario_code = 2  # medium scenario

        features = pd.DataFrame([{
            "routeLength": route_length_proxy,
            "duration": duration_proxy,
            "scenario": scenario_code,
            "vehicleCount": vehicle_count
        }])

        predicted_wait = model.predict(features)[0]
        predicted_wait = max(0, predicted_wait)

        print(f"Step {step} | Avg waiting: {avg_waiting:.2f} | Predicted waiting: {predicted_wait:.2f}")

        tls_ids = traci.trafficlight.getIDList()

        base_duration = 20
        max_adjustment = 20

        adjustment = min(max(predicted_wait, 0), max_adjustment)
        new_duration = base_duration + adjustment

        print(f"Applying phase duration: {new_duration:.2f}")

        for tls in tls_ids:
            traci.trafficlight.setPhaseDuration(tls, new_duration)

    step += 1

traci.close()