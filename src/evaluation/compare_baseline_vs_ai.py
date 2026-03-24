import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

pairs = [
    ("low", "ai_low"),
    ("medium", "ai_medium"),
    ("high", "ai_high"),
]

summary = []

for baseline_name, ai_name in pairs:
    baseline_file = Path(f"results/tripinfo_{baseline_name}.csv")
    ai_file = Path(f"results/tripinfo_{ai_name}.csv")

    if baseline_file.exists():
        df = pd.read_csv(baseline_file)
        summary.append({
            "scenario": baseline_name,
            "system": "baseline",
            "vehicles_completed": len(df),
            "avg_duration": df["duration"].mean(),
            "avg_waiting_time": df["waitingTime"].mean(),
            "avg_time_loss": df["timeLoss"].mean(),
        })

    if ai_file.exists():
        df = pd.read_csv(ai_file)
        summary.append({
            "scenario": baseline_name,
            "system": "ai",
            "vehicles_completed": len(df),
            "avg_duration": df["duration"].mean(),
            "avg_waiting_time": df["waitingTime"].mean(),
            "avg_time_loss": df["timeLoss"].mean(),
        })

summary_df = pd.DataFrame(summary)
print(summary_df)

summary_df.to_csv("results/baseline_vs_ai_summary.csv", index=False)

# Plot: average waiting time
pivot_wait = summary_df.pivot(index="scenario", columns="system", values="avg_waiting_time")
pivot_wait.plot(kind="bar")
plt.ylabel("Average Waiting Time")
plt.title("Baseline vs AI: Average Waiting Time")
plt.tight_layout()
plt.savefig("results/plots/baseline_vs_ai_waiting_time.png")
plt.show()

# Plot: average time loss
pivot_loss = summary_df.pivot(index="scenario", columns="system", values="avg_time_loss")
pivot_loss.plot(kind="bar")
plt.ylabel("Average Time Loss")
plt.title("Baseline vs AI: Average Time Loss")
plt.tight_layout()
plt.savefig("results/plots/baseline_vs_ai_time_loss.png")
plt.show()