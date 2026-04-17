import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

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

baseline_csv = Path("results/tripinfo_medium.csv")
old_rl_xml = Path("results/tripinfo_rl_medium_run1.xml")
improved_rl_xml = Path("results/tripinfo_rl_medium_improved.xml")
hierarchical_rl_xml = Path("results/tripinfo_hierarchical_rl_medium.xml")

if baseline_csv.exists():
    df = pd.read_csv(baseline_csv)
    summary.append({
        "system": "baseline_medium",
        "vehicles_completed": len(df),
        "avg_duration": df["duration"].mean(),
        "avg_waiting_time": df["waitingTime"].mean(),
        "avg_time_loss": df["timeLoss"].mean(),
    })

if old_rl_xml.exists():
    df = parse_tripinfo_xml(old_rl_xml)
    summary.append({
        "system": "old_rl_medium",
        "vehicles_completed": len(df),
        "avg_duration": df["duration"].mean(),
        "avg_waiting_time": df["waitingTime"].mean(),
        "avg_time_loss": df["timeLoss"].mean(),
    })

if improved_rl_xml.exists():
    df = parse_tripinfo_xml(improved_rl_xml)
    summary.append({
        "system": "improved_rl_medium",
        "vehicles_completed": len(df),
        "avg_duration": df["duration"].mean(),
        "avg_waiting_time": df["waitingTime"].mean(),
        "avg_time_loss": df["timeLoss"].mean(),
    })

if hierarchical_rl_xml.exists():
    df = parse_tripinfo_xml(hierarchical_rl_xml)
    summary.append({
        "system": "hierarchical_rl_medium",
        "vehicles_completed": len(df),
        "avg_duration": df["duration"].mean(),
        "avg_waiting_time": df["waitingTime"].mean(),
        "avg_time_loss": df["timeLoss"].mean(),
    })

summary_df = pd.DataFrame(summary)
print(summary_df)
summary_df.to_csv("results/hierarchical_rl_medium_summary.csv", index=False)
print("\nSaved to results/hierarchical_rl_medium_summary.csv")