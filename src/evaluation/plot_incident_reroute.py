import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

summary_file = Path("results/incident_reroute_summary.csv")
output_file = Path("results/plots/incident_reroute_waiting_time_comparison.png")

if not summary_file.exists():
    raise FileNotFoundError(f"Missing file: {summary_file}")

df = pd.read_csv(summary_file)

plt.figure(figsize=(7, 4))
plt.bar(df["system"], df["avg_waiting_time"])
plt.ylabel("Average Waiting Time")
plt.title("Incident Scenario: Baseline vs AI vs Reroute")
plt.tight_layout()
plt.savefig(output_file)
plt.show()

print(f"Saved plot to {output_file}")