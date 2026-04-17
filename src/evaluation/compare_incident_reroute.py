import pandas as pd
from pathlib import Path

files = {
    "incident_baseline": Path("results/tripinfo_incident_baseline.csv"),
    "incident_ai": Path("results/tripinfo_incident_ai.csv"),
    "incident_reroute": Path("results/tripinfo_incident_reroute.csv"),
}

summary = []

for system, file in files.items():
    if file.exists():
        df = pd.read_csv(file)
        summary.append({
            "system": system,
            "vehicles_completed": len(df),
            "avg_duration": df["duration"].mean(),
            "avg_waiting_time": df["waitingTime"].mean(),
            "avg_time_loss": df["timeLoss"].mean(),
        })
    else:
        print(f"Missing file: {file}")

summary_df = pd.DataFrame(summary)
print(summary_df)
summary_df.to_csv("results/incident_reroute_summary.csv", index=False)
print("\nSaved to results/incident_reroute_summary.csv")