import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("results/dataset.csv")

# Convert scenario to numeric
df["scenario"] = df["scenario"].map({
    "low": 0,
    "medium": 1,
    "high": 2
})

# Features and target
X = df[["routeLength", "duration", "scenario"]]
y = df["waitingTime"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)

print("Model trained")
print("Mean Absolute Error:", mae)