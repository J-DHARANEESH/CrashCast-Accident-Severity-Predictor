# 🚗 CrashCast: Accident Severity Prediction Using ML

**CrashCast** is a machine learning-powered Flask application and Power BI dashboard for predicting and analyzing the severity of road accidents. It leverages weather, traffic, and road conditions to assess accident risk levels in real time and offers rich insights into patterns and trends.

---

## 🔍 Key Features

### ✅ Flask Prediction App

* Predicts accident severity (Low, Moderate, High)
* REST API for integration
* Real-time prediction using trained ML model
* Input features include:

  * Weather Condition, Visibility, Wind Speed
  * Road Features (e.g., Junction, Crossing, etc.)
  * Environmental attributes like Sunrise/Sunset

### 📊 Power BI Dashboard

* No live model predictions; purely analytical
* Visualizes:

  * Accident severity distribution
  * Monthly and time-of-day accident patterns
  * Weather type breakdown
  * Most affected counties and states
  * Visibility & precipitation vs severity

---

## 🖼️ Screenshots

### 🔹 Flask Web App

> Accident Severity Prediction Form

![image](https://github.com/user-attachments/assets/acc72fc2-512b-4e1f-955d-258d138f13ac)


---

### 🔹 Power BI Dashboard

> Road Accident Patterns and Trends Analysis

![image](https://github.com/user-attachments/assets/fa9b2838-9dfd-4726-b948-8400e759c628)


📝 **Download Dashboard**:
[👉 Accident Patterns and Trends Dashboard.pbix (Google Drive)](https://drive.google.com/drive/folders/12wICmB5CzhMjFxqMQsX2rUxw7RE00XHd)

---

## 🧠 ML Model Details

* **Algorithm**: Random Forest Classifier
* **Data**: [US Accidents Dataset – Kaggle](https://www.kaggle.com/sobhanmoosavi/us-accidents)
* **Preprocessing**:

  * Label Encoding (for categorical features)
  * StandardScaler (for numerical features)
* **Features**:

  * `Temperature(F)`, `Humidity(%)`, `Pressure(in)`
  * `Visibility(mi)`, `Wind_Speed(mph)`
  * Road & weather conditions

---

## 🚀 How to Run the App

### 1. Clone the Project

```bash
git clone https://github.com/J-DHARANEESH/CrashCast-Accident-Severity-Predictor.git
cd CrashCast-Accident-Severity-Predictor
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python app.py
```

Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔌 API Usage

**POST** `/predict`
Content-Type: `application/json`

#### Example Payload:

```json
{
  "Temperature(F)": 65,
  "Humidity(%)": 60,
  "Pressure(in)": 29.9,
  "Visibility(mi)": 10,
  "Wind_Speed(mph)": 5,
  "Weather_Condition": "Rain",
  "Amenity": "False",
  "Bump": "False",
  "Crossing": "True",
  "Junction": "True",
  "Traffic_Signal": "True",
  "Sunrise_Sunset": "Night"
}
```

#### Example Response:

```json
{
  "predicted_severity": 3
}
```

---

## 📁 Project Structure

```
├── app.py
├── requirements.txt
├── dashboard/
│   └── Accident Patterns and Trends Dashboard.pbix
├── dataset/
├── model/
│   ├── accident_severity_model.pkl
│   ├── scaler.pkl
│   └── [feature]_label_encoder.pkl
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── notebooks/
│   └── accident_severity_training.ipynb
└── README.md
```

---

## 🧪 Power BI Dashboard Explained

1. **Casualties by Severity**:
   Bar chart showing total casualties grouped by severity (1–4 scale).

2. **Key KPIs**:

   * Total casualties
   * Most affected county
   * Total fatal accidents
   * Most common severity level

3. **Monthly Trends**:
   Line graph showing how casualties vary across months.

4. **Time of Day Analysis**:
   Pie chart showing day vs night accident ratios.

5. **Weather Types**:
   Pie chart of accidents categorized into weather types like:

   * Rain, Snow, Cloudy, Clear, Foggy, Freezing Rain, Other

6. **Road Features Impact**:
   Bar chart highlighting how certain road features (e.g., Junctions, Crossings) relate to accident counts.

7. **Precipitation & Visibility vs Severity**:
   Scatter plot correlating severity levels with average visibility and precipitation.

---

## 📌 Future Enhancements

* Hyperparameter tuning for improved accuracy
* Host model on cloud platforms (AWS/Heroku)
* Add accident heatmaps or clustering on dashboard
* Integrate predictions directly into Power BI using a live REST API

---

## 📝 License

Licensed under the [MIT License](LICENSE).

---

