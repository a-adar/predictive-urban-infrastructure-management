import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

input_dir = Path("results")
output_rows = []

for xml_file in input_dir.glob("tripinfo_*.xml"):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    rows = []
    for trip in root.findall("tripinfo"):
        rows.append({
            "duration": float(trip.get("duration", 0)),
            "waitingTime": float(trip.get("waitingTime", 0)),
            "timeLoss": float(trip.get("timeLoss", 0)),
            "routeLength": float(trip.get("routeLength", 0)),
        })

    if rows:
        df = pd.DataFrame(rows)

        # Remove "tripinfo_" prefix only
        run_name = xml_file.stem.replace("tripinfo_", "")

        output_rows.append({
            "run_name": run_name,
            "vehicles_completed": len(df),
            "avg_duration": df["duration"].mean(),
            "avg_waiting_time": df["waitingTime"].mean(),
            "avg_time_loss": df["timeLoss"].mean(),
            "std_waiting_time": df["waitingTime"].std(),
        })

summary_df = pd.DataFrame(output_rows)
summary_df.to_csv("results/repeated_runs_summary.csv", index=False)
print(summary_df)
print("\nSaved to results/repeated_runs_summary.csv")