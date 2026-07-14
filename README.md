# 🏢 Building Cooling Load Prediction

A Machine Learning web application that predicts the **Cooling Load** of a building based on its structural characteristics. This project uses the **UCI Energy Efficiency Dataset** and compares multiple regression algorithms to identify the best-performing model.

## 🚀 Live Demo

**Streamlit App:**  
https://building-cooling-load-prediction-7rtpboqumxoerlbcjp3who.streamlit.app

---

## 📌 Project Overview

Cooling load prediction is an important task in building energy management. Accurate predictions help engineers design energy-efficient buildings and optimize HVAC systems.

This project:
- Performs data exploration and analysis.
- Trains multiple machine learning models.
- Compares model performance using evaluation metrics.
- Deploys the best model as an interactive Streamlit web application.

---

## 📂 Dataset

**Dataset:** UCI Energy Efficiency Dataset

The dataset contains **768 building designs** with various structural features and corresponding heating and cooling loads.

### Features Used

- Relative Compactness
- Surface Area
- Wall Area
- Roof Area
- Overall Height
- Glazing Area

### Target Variable

- Cooling Load

---

## 🤖 Machine Learning Models

The following regression models were trained and compared:

- Linear Regression
- Decision Tree Regressor ✅ (Selected Model)
- Random Forest Regressor

---

## 📊 Model Performance

| Model | MAE | RMSE | R² Score |
|--------|-----:|------:|---------:|
| Linear Regression | 2.2012 | 3.1550 | 0.8926 |
| Decision Tree Regressor | **1.1654** | **1.7481** | **0.9670** |
| Random Forest Regressor | 1.1701 | 1.7494 | 0.9670 |

The **Decision Tree Regressor** achieved the best performance and was selected for deployment.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib

---

## 📁 Project Structure

```
Building-Cooling-Load-Prediction/
│
├── app.py
├── cooling_load_prediction.ipynb
├── decision_tree_cooling_model.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🎯 Features

- User-friendly Streamlit interface
- Real-time cooling load prediction
- Interactive input fields
- Machine learning-based prediction
- Responsive web application

---

## 📷 Application Preview



```
app_preview.png
```

---

## 👨‍💻 Author

**Mubashir Ali**

Mechanical Engineer | Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.
