import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = pd.DataFrame({
    "attendance": [85, 60, 90, 55],
    "marks": [78, 50, 88, 45],
    "engagement": [70, 40, 85, 35],
    "result": [1, 0, 1, 0]
})

X = data[["attendance", "marks", "engagement"]]
y = data["result"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully ✅")