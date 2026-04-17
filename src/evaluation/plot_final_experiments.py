import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("results/final_experiment_summary.csv")
Path("results/plots").mkdir(parents=True, exist_ok=True)

# Waiting time plot
pivot_wait = df.pivot(index="scenario", columns="system", values="avg_waiting_time_mean")
pivot_wait.plot(kind="bar")
plt.ylabel("Average Waiting Time")
plt.title("Average Waiting Time by Scenario and System")
plt.tight_layout()
plt.savefig("results/plots/final_avg_waiting_time.png")
plt.show()

# Time loss plot
pivot_loss = df.pivot(index="scenario", columns="system", values="avg_time_loss_mean")
pivot_loss.plot(kind="bar")
plt.ylabel("Average Time Loss")
plt.title("Average Time Loss by Scenario and System")
plt.tight_layout()
plt.savefig("results/plots/final_avg_time_loss.png")
plt.show()

# Vehicles completed plot
pivot_vehicles = df.pivot(index="scenario", columns="system", values="vehicles_completed_mean")
pivot_vehicles.plot(kind="bar")
plt.ylabel("Vehicles Completed")
plt.title("Vehicles Completed by Scenario and System")
plt.tight_layout()
plt.savefig("results/plots/final_vehicles_completed.png")
plt.show()

# Stability plot
pivot_std = df.pivot(index="scenario", columns="system", values="std_waiting_time_mean")
pivot_std.plot(kind="bar")
plt.ylabel("Std. Dev. of Waiting Time")
plt.title("Waiting Time Stability by Scenario and System")
plt.tight_layout()
plt.savefig("results/plots/final_waiting_time_stability.png")
plt.show()

print("Saved final RL-inclusive plots to results/plots/")