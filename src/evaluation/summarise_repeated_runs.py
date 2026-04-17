import pandas as pd

df = pd.read_csv("results/repeated_runs_summary.csv")

def infer_system(name: str) -> str:
    if name.startswith("rl_"):
        return "rl"
    if name.startswith("ai_"):
        return "ai"
    if name.startswith("no_ml_"):
        return "adaptive_no_ml"
    return "baseline"

def infer_scenario(name: str) -> str:
    if "incident" in name:
        return "incident"
    if "low" in name:
        return "low"
    if "medium" in name:
        return "medium"
    if "high" in name:
        return "high"
    return "unknown"

df["system"] = df["run_name"].apply(infer_system)
df["scenario"] = df["run_name"].apply(infer_scenario)

grouped = df.groupby(["scenario", "system"]).agg({
    "vehicles_completed": ["mean", "std"],
    "avg_duration": ["mean", "std"],
    "avg_waiting_time": ["mean", "std"],
    "avg_time_loss": ["mean", "std"],
    "std_waiting_time": ["mean", "std"],
}).reset_index()

grouped.columns = [
    "scenario", "system",
    "vehicles_completed_mean", "vehicles_completed_std",
    "avg_duration_mean", "avg_duration_std",
    "avg_waiting_time_mean", "avg_waiting_time_std",
    "avg_time_loss_mean", "avg_time_loss_std",
    "std_waiting_time_mean", "std_waiting_time_std",
]

grouped.to_csv("results/final_experiment_summary.csv", index=False)
print(grouped)
print("\nSaved to results/final_experiment_summary.csv")