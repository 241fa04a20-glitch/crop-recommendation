import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("crop_data.csv")

# Split features & target
X = data.drop("label", axis=1)
y = data["label"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# CREATE MODEL FIRST ✅
model = RandomForestClassifier(n_estimators=100)

# TRAIN MODEL ✅
model.fit(X_train, y_train)

# NOW predict ✅
pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")