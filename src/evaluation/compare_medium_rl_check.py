import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def parse_tripinfo_xml(xml_path: Path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    rows = []
    for trip in root.findall("tripinfo"):
        rows.append({
            "duration": float(trip.get("duration", 0)),
            "waitingTime": float(trip.get("waitingTime", 0)),
            "timeLoss": float(trip.get("timeLoss", 0)),
            "routeLength": float(trip.get("routeLength", 0)),
        })

    return pd.DataFrame(rows)

summary = []

# 1. Baseline medium CSV already exists
baseline_csv = Path("results/tripinfo_medium.csv")
if baseline_csv.exists():
    df = pd.read_csv(baseline_csv)
    summary.append({
        "system": "baseline_medium",
        "vehicles_completed": len(df),
        "avg_duration": df["duration"].mean(),
        "avg_waiting_time": df["waitingTime"].mean(),
        "avg_time_loss": df["timeLoss"].mean(),
    })
else:
    print(f"Missing file: {baseline_csv}")

# 2. Old RL medium XML
old_rl_xml = Path("results/tripinfo_rl_medium_run1.xml")
if old_rl_xml.exists():
    df = parse_tripinfo_xml(old_rl_xml)
    summary.append({
        "system": "old_rl_medium",
        "vehicles_completed": len(df),
        "avg_duration": df["duration"].mean(),
        "avg_waiting_time": df["waitingTime"].mean(),
        "avg_time_loss": df["timeLoss"].mean(),
    })
else:
    print(f"Missing file: {old_rl_xml}")

# 3. Improved RL medium XML
improved_rl_xml = Path("results/tripinfo_rl_medium_improved.xml")
if improved_rl_xml.exists():
    df = parse_tripinfo_xml(improved_rl_xml)
    summary.append({
        "system": "improved_rl_medium",
        "vehicles_completed": len(df),
        "avg_duration": df["duration"].mean(),
        "avg_waiting_time": df["waitingTime"].mean(),
        "avg_time_loss": df["timeLoss"].mean(),
    })
else:
    print(f"Missing file: {improved_rl_xml}")

summary_df = pd.DataFrame(summary)
print(summary_df)

summary_df.to_csv("results/medium_rl_check_summary.csv", index=False)
print("\nSaved to results/medium_rl_check_summary.csv")

plt.figure(figsize=(7, 4))
plt.bar(summary_df["system"], summary_df["avg_waiting_time"])
plt.ylabel("Average Waiting Time")
plt.title("Medium Scenario: Baseline vs Old RL vs Improved RL")
plt.tight_layout()
plt.savefig("results/plots/medium_rl_check_waiting_time.png")
plt.show()

print("Saved plot to results/plots/medium_rl_check_waiting_time.png")