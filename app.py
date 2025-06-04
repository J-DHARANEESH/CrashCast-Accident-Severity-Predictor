from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Paths
MODEL_PATH = os.path.join( 'model', 'accident_severity_model.pkl')
SCALER_PATH = os.path.join( 'model', 'scaler.pkl')

categorical_features = ['Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Junction', 'Traffic_Signal', 'Sunrise_Sunset']
numerical_features = ['Temperature(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)']

# Load model, scaler, encoders
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoders = {}
for col in categorical_features:
    encoder_path = os.path.join( 'model', f"{col}_label_encoder.pkl")
    label_encoders[col] = joblib.load(encoder_path)


def preprocess(input_data):
    features = []

    # Encode categorical
    for col in categorical_features:
        val = input_data.get(col, '')
        if val == '':
            val = 'unknown'
        try:
            encoded_val = label_encoders[col].transform([str(val)])[0]
        except ValueError:
            encoded_val = 0
        features.append(encoded_val)

    # Append numerical
    for col in numerical_features:
        try:
            features.append(float(input_data.get(col, 0)))
        except (ValueError, TypeError):
            features.append(0.0)

    features_array = np.array(features).reshape(1, -1)
    return scaler.transform(features_array)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form.to_dict()
        input_data = {}

        for col in categorical_features + numerical_features:
            input_data[col] = data.get(col)

        try:
            processed = preprocess(input_data)
            prediction = int(model.predict(processed)[0])
            return render_template('index.html', prediction=prediction, input_data=input_data)
        except Exception as e:
            return render_template('index.html', error=str(e), input_data=input_data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
