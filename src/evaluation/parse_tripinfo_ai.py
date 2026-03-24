import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

def parse_tripinfo(xml_path, csv_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    rows = []

    for trip in root.findall("tripinfo"):
        rows.append({
            "id": trip.get("id"),
            "depart": float(trip.get("depart", 0)),
            "arrival": float(trip.get("arrival", 0)),
            "duration": float(trip.get("duration", 0)),
            "waitingTime": float(trip.get("waitingTime", 0)),
            "timeLoss": float(trip.get("timeLoss", 0)),
            "routeLength": float(trip.get("routeLength", 0)),
        })

    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)

    return df

files = {
    "low": "results/tripinfo_low.xml",
    "medium": "results/tripinfo_medium.xml",
    "high": "results/tripinfo_high.xml",
    "ai_low": "results/tripinfo_ai_low.xml",
    "ai_medium": "results/tripinfo_ai_medium.xml",
    "ai_high": "results/tripinfo_ai_high.xml",
    "incident_baseline": "results/tripinfo_incident_baseline.xml",
    "incident_ai": "results/tripinfo_incident_ai.xml",
}

for scenario, path in files.items():
    xml_file = Path(path)
    csv_file = Path(f"results/tripinfo_{scenario}.csv")

    if xml_file.exists():
        df = parse_tripinfo(xml_file, csv_file)
        print(f"\nScenario: {scenario}")
        print("Vehicles completed:", len(df))
        print("Average duration:", df["duration"].mean())
        print("Average waiting time:", df["waitingTime"].mean())
        print("Average time loss:", df["timeLoss"].mean())
    else:
        print(f"\nSkipping {scenario}: file not found -> {xml_file}")