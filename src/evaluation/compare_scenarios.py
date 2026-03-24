import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

scenarios = ["low", "medium", "high"]
summary = []

for scenario in scenarios:
    file = Path(f"results/tripinfo_{scenario}.csv")
    if file.exists():
        df = pd.read_csv(file)
        summary.append({
            "scenario": scenario,
            "vehicles_completed": len(df),
            "avg_duration": df["duration"].mean(),
            "avg_waiting_time": df["waitingTime"].mean(),
            "avg_time_loss": df["timeLoss"].mean(),
        })

summary_df = pd.DataFrame(summary)
print(summary_df)

summary_df.to_csv("results/scenario_summary.csv", index=False)

plt.figure(figsize=(8, 5))
plt.bar(summary_df["scenario"], summary_df["avg_waiting_time"])
plt.xlabel("Scenario")
plt.ylabel("Average Waiting Time")
plt.title("Average Waiting Time by Traffic Scenario")
plt.tight_layout()
plt.savefig("results/plots/avg_waiting_time_by_scenario.png")
plt.show()