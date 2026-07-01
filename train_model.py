from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample training data
X = [
    [80, 75, 70],
    [50, 40, 30],
    [90, 85, 88],
    [40, 30, 20]
]

y = [1, 0, 1, 0]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model created successfully!")