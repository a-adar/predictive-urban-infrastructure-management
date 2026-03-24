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

    if step % CONTROL_INTERVAL == 0:
        route_length_proxy = 100
        duration_proxy = avg_waiting * 100
        scenario_code = 1  # medium scenario

        features = pd.DataFrame([{
            "routeLength": route_length_proxy,
            "duration": duration_proxy,
            "scenario": scenario_code
        }])

        predicted_wait = model.predict(features)[0]
        predicted_wait = max(0, predicted_wait)

        print(f"Step {step} | Avg waiting: {avg_waiting:.2f} | Predicted waiting: {predicted_wait:.2f}")

        tls_ids = traci.trafficlight.getIDList()

        if predicted_wait > 10:
            if current_mode != "congested":
                print("Switching to CONGESTED mode")
                for tls in tls_ids:
                    traci.trafficlight.setPhaseDuration(tls, 40)
                current_mode = "congested"
        else:
            if current_mode != "normal":
                print("Switching to NORMAL mode")
                for tls in tls_ids:
                    traci.trafficlight.setPhaseDuration(tls, 20)
                current_mode = "normal"

    step += 1

traci.close()