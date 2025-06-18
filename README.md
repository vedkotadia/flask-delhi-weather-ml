
# Delhi Weather Prediction Web App

This is a Flask-based web application that predicts the temperature (in Celsius) in Delhi using input features such as humidity, wind speed, pressure, month, and day of the year. The prediction is powered by a pre-trained machine learning model.

---

## 🔥 Features

- User-friendly web interface  
- Predicts Delhi temperature based on 5 input values  
- Built with Flask and scikit-learn  
- Machine learning model with **R² score: 0.94**

---

## 📁 Files

- `app.py` – Flask application  
- `delhi_weather_model.pkl` – Pre-trained regression model  
- `feature_scaler.pkl` – Feature scaling transformer  
- `templates/index.html` – HTML form for user input  

---

## 📦 Requirements

Install dependencies with:

```bash
pip install flask numpy scikit-learn joblib
```

---

## ▶️ How to Run

```bash
python app.py
```

Then open your browser and visit:  
`http://127.0.0.1:5000`

---

## 🧪 Usage

1. Enter the following inputs:
   - Humidity  
   - Wind Speed  
   - Mean Pressure  
   - Month (1–12)  
   - Day of the Year (1–365)  

2. Submit the form to get the predicted temperature in Celsius.

---

## 🖼️ Screenshots

### Input Form

![Input Form](weather_web/Screenshot%202025-06-19%20000011.png)

### Prediction Result

![Prediction Result](weather_web/Screenshot%202025-06-19%20000021.png)

---

## ⚠️ Error Handling

If invalid (non-numeric) values are entered, a user-friendly error message will be displayed.

---


