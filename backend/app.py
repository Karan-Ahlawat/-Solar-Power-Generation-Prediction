from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import pandas as pd

app = Flask(__name__)

CORS(app)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH_1 = os.path.join(
    BASE_DIR,
    "random_forest_model.pkl"
)

MODEL_PATH_2 = os.path.join(
    BASE_DIR,
    "random_forest_model_plant_2.pkl"
)

model_1 = joblib.load(MODEL_PATH_1)
model_2 = joblib.load(MODEL_PATH_2) if os.path.exists(MODEL_PATH_2) else model_1


@app.route("/")
def home():
    return "Solar Prediction Backend is running! Supporting Plant 1 & Plant 2."


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = pd.DataFrame([{
        "SOURCE_KEY_x": data["SOURCE_KEY_x"],
        "AMBIENT_TEMPERATURE": data["AMBIENT_TEMPERATURE"],
        "MODULE_TEMPERATURE": data["MODULE_TEMPERATURE"],
        "IRRADIATION": data["IRRADIATION"],
        "HOUR": data["HOUR"],
        "DAY": data["DAY"],
        "MONTH": data["MONTH"],
        "WEEKDAY": data["WEEKDAY"],
        "IS_WEEKEND": data["IS_WEEKEND"]
    }])

    plant = data.get("PLANT_ID", data.get("plant_id", data.get("plant", 1)))
    is_plant_2 = plant in [2, "2", 4136001, "4136001", "Plant 2", "plant_2"]

    selected_model = model_2 if is_plant_2 else model_1
    prediction = selected_model.predict(features)[0]

    return jsonify({
        "predicted_ac_power": float(prediction),
        "plant": 2 if is_plant_2 else 1
    })


if __name__ == "__main__":
    app.run(
        debug=True
    )
