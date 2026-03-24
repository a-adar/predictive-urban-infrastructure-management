import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

input_file = Path("results/tripinfo_medium.csv")
output_file = Path("results/plots/medium_waiting_time_histogram.png")

df = pd.read_csv(input_file)

plt.figure(figsize=(8, 5))
plt.hist(df["waitingTime"], bins=20)
plt.xlabel("Waiting Time")
plt.ylabel("Number of Vehicles")
plt.title("Distribution of Vehicle Waiting Times (Medium Traffic)")
plt.tight_layout()

output_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_file)
plt.show()

print("Saved plot to:", output_file)