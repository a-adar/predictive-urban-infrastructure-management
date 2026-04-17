import traci

SUMO_CONFIG = "simulation/configs/chicago_incident.sumocfg"

# Replace with your actual chosen edge
INCIDENT_EDGE = "433783093#1"

INCIDENT_START = 610
INCIDENT_END = 1688
REROUTE_INTERVAL = 3

incident_active = False

def vehicle_needs_reroute(veh_id: str, closed_edge: str) -> bool:
    """
    True if the vehicle's remaining route still contains the closed edge.
    """
    try:
        route = traci.vehicle.getRoute(veh_id)
        current_edge = traci.vehicle.getRoadID(veh_id)

        if current_edge not in route:
            return closed_edge in route

        current_index = route.index(current_edge)
        remaining_route = route[current_index + 1:]
        return closed_edge in remaining_route
    except traci.TraCIException:
        return False

def reroute_affected_vehicles(closed_edge: str):
    vehicle_ids = traci.vehicle.getIDList()
    affected = 0
    rerouted = 0
    failed = 0

    for vid in vehicle_ids:
        try:
            current_edge = traci.vehicle.getRoadID(vid)

            # Let vehicles already on the closed edge finish it
            if current_edge == closed_edge:
                continue

            if vehicle_needs_reroute(vid, closed_edge):
                affected += 1
                traci.vehicle.rerouteTraveltime(vid)
                rerouted += 1
        except traci.TraCIException:
            failed += 1

    print(f"Affected vehicles: {affected}")
    print(f"Successfully rerouted: {rerouted}")
    print(f"Failed reroutes: {failed}")

traci.start(["sumo-gui", "-c", SUMO_CONFIG])

step = 0

try:
    while step < 3600:
        traci.simulationStep()

        # Start closure
        if step == INCIDENT_START and not incident_active:
            print(f"Starting incident at step {step} on edge {INCIDENT_EDGE}")

            if INCIDENT_EDGE not in traci.edge.getIDList():
                print(f"ERROR: edge {INCIDENT_EDGE} not found in network.")
                break

            traci.edge.setDisallowed(INCIDENT_EDGE, ["passenger"])
            incident_active = True

            # Initial reroute
            reroute_affected_vehicles(INCIDENT_EDGE)

        # Keep rerouting during closure so new vehicles are handled too
        if incident_active and step > INCIDENT_START and step % REROUTE_INTERVAL == 0:
            print(f"Periodic reroute check at step {step}")
            reroute_affected_vehicles(INCIDENT_EDGE)

        # Optional reopening
        if step == INCIDENT_END and incident_active:
            print(f"Ending incident at step {step} on edge {INCIDENT_EDGE}")

            traci.edge.setAllowed(INCIDENT_EDGE, ["passenger"])
            incident_active = False

            # Reroute again after reopening
            vehicle_ids = traci.vehicle.getIDList()
            rerouted = 0
            failed = 0

            for vid in vehicle_ids:
                try:
                    traci.vehicle.rerouteTraveltime(vid)
                    rerouted += 1
                except traci.TraCIException:
                    failed += 1

            print(f"Vehicles rerouted after reopening: {rerouted}")
            print(f"Failed reroutes after reopening: {failed}")

        step += 1

except traci.exceptions.FatalTraCIError as e:
    print("SUMO closed unexpectedly.")
    print("This usually means the chosen edge is too critical and some later vehicle had no valid alternative route.")
    print("Try a different edge with more nearby alternatives.")
    print("Error:", e)

finally:
    try:
        traci.close()
    except:
        pass