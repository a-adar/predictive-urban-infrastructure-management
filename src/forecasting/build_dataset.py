import pandas as pd
from pathlib import Path

files = {
    "low": "results/tripinfo_low.csv",
    "medium": "results/tripinfo_medium.csv",
    "high": "results/tripinfo_high.csv"
}

dfs = []

for scenario, path in files.items():
    file = Path(path)
    if file.exists():
        df = pd.read_csv(file)
        df["scenario"] = scenario
        dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

# Save combined dataset
data.to_csv("results/dataset.csv", index=False)

print("Dataset created:", data.shape)
print(data.head())