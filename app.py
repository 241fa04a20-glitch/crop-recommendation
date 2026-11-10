from flask import Flask, render_template, request
import pickle
import numpy as np
from pymongo import MongoClient

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cropDB"]
collection = db["predictions"]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input
        features = [float(x) for x in request.form.values()]
        final = [features]

        # Predict
        prediction = model.predict(final)[0]

        # Save to DB
        collection.insert_one({
            "N": features[0],
            "P": features[1],
            "K": features[2],
            "temperature": features[3],
            "humidity": features[4],
            "ph": features[5],
            "rainfall": features[6],
            "prediction": prediction
        })

        return render_template("index.html", prediction=prediction)

    except Exception as e:
        return render_template("index.html", prediction="Error")

if __name__ == "__main__":
    app.run(debug=True)