import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("results/dataset.csv")

df["scenario"] = df["scenario"].map({
    "low": 0,
    "medium": 1,
    "high": 2
})

X = df[["routeLength", "duration", "scenario"]]
y = df["waitingTime"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Waiting Time")
plt.ylabel("Predicted Waiting Time")
plt.title("Prediction vs Actual Waiting Time")
plt.show()