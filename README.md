# 🏡 California Housing Price Prediction

This project builds a **machine learning application** to predict **California house prices** using the **California Housing Dataset**.  
It includes both **regression** and **classification** models along with a **Streamlit web interface**.

---

## 📌 Project Overview

The project demonstrates:

- 📈 **Linear Regression** to predict house prices (in dollars)
- 📊 **Logistic Regression** to classify houses as **High Price** or **Low Price**
- 🖥️ **Streamlit App** for interactive user input and predictions

---

## 📂 Project Structure

```
├── app.py                         # Streamlit application
├── linear_regression_model.pkl    # Trained Linear Regression model
├── logistic_regression_model.pkl  # Trained Logistic Regression model
├── california_housing.ipynb       # Model training notebook
├── README.md                      # Project documentation
```

---

## 📊 Dataset

**California Housing Dataset**  
Source: 1990 California Census (`sklearn.datasets.fetch_california_housing`)

### 🔹 Features Used

| Feature   | Description                                     |
| --------- | ----------------------------------------------- |
| MedInc    | Median income (in tens of thousands of dollars) |
| HouseAge  | Median age of houses                            |
| AveRooms  | Average number of rooms per household           |
| AveBedrms | Average number of bedrooms per household        |

### 🎯 Target Variable

| Variable | Description                          |
| -------- | ------------------------------------ |
| PRICE    | Median house value in **US dollars** |

```python
df["PRICE"] = housing.target * 100000
```

---

## 🧠 Models Used

### 1️⃣ Linear Regression

- Predicts **house prices in dollars**
- Evaluation Metrics:
  - Mean Squared Error (MSE)
  - R² Score

### 2️⃣ Logistic Regression

- Binary classification:
  - `1` → High Price
  - `0` → Low Price
- Threshold: Median house price
- Evaluation Metric:
  - Accuracy Score

---

## ⚙️ Data Preprocessing

- Converted target variable to **dollars**
- Ensured **unit consistency** across:
  - Training
  - Testing
  - Prediction
  - Visualization

---

## 📈 Model Evaluation

### Linear Regression

- Scatter plot: **Actual vs Predicted Prices**
- Perfect prediction reference line (y = x)

### Logistic Regression

- Confusion matrix visualization
- Accuracy score

---

## 🖥️ Streamlit Web Application

### 🔹 Features

- User-friendly interface
- Median Income entered in **real dollars**
- Automatic conversion to dataset scale

```python
user_income = st.number_input("Median Income ($)", value=60000)
medinc = user_income / 10000
```

- Outputs:
  - 🏠 Predicted house price
  - 📈 Price category (High / Low)

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🛠️ Installation & Requirements

```bash
pip install numpy pandas matplotlib seaborn scikit-learn streamlit
```

---

## ✅ Results & Insights

- **Median Income** is the most influential feature
- Linear Regression provides reasonable price predictions
- Logistic Regression effectively classifies high vs low price houses

---

## 🚀 Future Improvements

- Add geographic features (Latitude, Longitude)
- Hyperparameter tuning
- SHAP feature importance analysis
- Try advanced models (Random Forest, XGBoost)

---
