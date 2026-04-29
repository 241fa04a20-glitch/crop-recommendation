<<<<<<< HEAD
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("crop_data.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

=======
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("crop_data.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

>>>>>>> 66181f0678e40c9a70b2d68878615fdf23b77ecb
print("Model trained successfully!")