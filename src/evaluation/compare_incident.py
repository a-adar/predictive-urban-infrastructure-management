import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

files = {
    "baseline": Path("results/tripinfo_incident_baseline.csv"),
    "ai": Path("results/tripinfo_incident_ai.csv"),
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

summary_df = pd.DataFrame(summary)
print(summary_df)

summary_df.to_csv("results/incident_summary.csv", index=False)

plt.figure(figsize=(6, 4))
plt.bar(summary_df["system"], summary_df["avg_waiting_time"])
plt.ylabel("Average Waiting Time")
plt.title("Incident Scenario: Baseline vs AI")
plt.tight_layout()
plt.savefig("results/plots/incident_waiting_time_comparison.png")
plt.show()