from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("delhi_weather_model.pkl")
scaler = joblib.load("feature_scaler.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            # Collect and convert inputs
            humidity = float(request.form['humidity'])
            wind_speed = float(request.form['wind_speed'])
            meanpressure = float(request.form['meanpressure'])
            month = int(request.form['month'])
            dayofyear = int(request.form['dayofyear'])

            # Create input array
            X = np.array([[humidity, wind_speed, meanpressure, month, dayofyear]])

            # Scale and predict
            X_scaled = scaler.transform(X)
            y_pred = model.predict(X_scaled)

            prediction = f"{y_pred[0]:.2f} °C"
        except Exception as e:
            print("Prediction error:", e)
            error = "Invalid input. Please enter valid numbers."

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
