from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import joblib
import traceback
import inflect

app = Flask(__name__)
CORS(app)
p = inflect.engine()

# Load the trained model, encoders, scaler, and expected columns
model = joblib.load("model.pkl")
le_dict = joblib.load("Encoder.pkl")
scaler = joblib.load("scaler.pkl")
X_columns = joblib.load("columns.pkl")  # pre-saved during model training

@app.route('/')
def home():
    return render_template('index.html')

# Prediction Endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        input_df = pd.DataFrame([data])

        # Encode using same LabelEncoders
        for col in le_dict:
            if col in input_df:
                if input_df[col][0] in le_dict[col].classes_:
                    input_df[col] = le_dict[col].transform([input_df[col][0]])
                else:
                    return jsonify({"error": f"Invalid value for '{col}': {input_df[col][0]}"})

        # Ensure all columns exist in correct order
        input_df = input_df[X_columns]

        # Scale the input
        input_scaled = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(input_scaled)[0]

        # Format prediction
        prediction_rounded = round(prediction, 2)
        prediction_in_words = p.number_to_words(int(prediction_rounded))

        return jsonify({
            "prediction": prediction_rounded,
            "prediction_in_words": prediction_in_words + " rupees"
        })

    except Exception as e:
        return jsonify({"error": str(e), "trace": traceback.format_exc()})

if __name__ == "__main__":
    app.run(debug=True)
