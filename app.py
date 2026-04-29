from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cropDB"]
collection = db["history"]
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    collection.insert_one({
    "input": features,
    "prediction": prediction
})
    try:
        features = [float(x) for x in request.form.values()]
        final = [np.array(features)]

        prediction = model.predict(final)[0]

        return render_template("index.html", prediction=prediction)
    
    except:
        return render_template("index.html", prediction="Invalid Input")

if __name__ == "__main__":
    app.run(debug=True)