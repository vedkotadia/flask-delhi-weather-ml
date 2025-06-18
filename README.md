# flask-delhi-weather-ml
A Flask web app that predicts Delhi’s temperature using a machine learning model (R² score: 0.94) based on humidity, wind speed, pressure, month, and day of the year.

Features
- User-friendly web interface
- Predicts Delhi temperature based on 5 inputs
- Uses a trained machine learning model (delhi_weather_model.pkl) and a feature scaler (feature_scaler.pkl)
  
Files
- app.py: Main Flask application
- delhi_weather_model.pkl: Trained machine learning model (serialized with joblib)
- feature_scaler.pkl: Pre-fitted feature scaler (e.g., StandardScaler or MinMaxScaler)
- templates/index.html: HTML form for user inputs
  
Requirements
- Python 3.x
- Flask
- NumPy
- scikit-learn
- joblib
  
Install requirements:
pip install flask numpy scikit-learn joblib
Delhi Weather Prediction Web App

How to Run
1. Ensure all files (app.py, delhi_weather_model.pkl, feature_scaler.pkl, and the templates/ folder) are in the
same directory.
2. Run the Flask app:
python app.py
3. Open your browser and go to http://127.0.0.1:5000
   
Usage
1. Enter the following inputs:
- Humidity
- Wind Speed
- Mean Pressure
- Month (1-12)
- Day of Year (1-365)
2. Submit the form to get the predicted temperature in Celsius.
  ## Input Form Example

![Input Form]("C:\Users\Ved Kotadia\Documents\weather_web\Screenshot 2025-06-19 000011.png")

## Prediction Result Example

![Prediction Result]("C:\Users\Ved Kotadia\Documents\weather_web\Screenshot 2025-06-19 000021.png")


