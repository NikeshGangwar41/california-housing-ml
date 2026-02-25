# 🏡 California Housing Price Prediction (Random Forest)

This project builds a **Machine Learning web application** to predict **California house prices** using the **California Housing Dataset**.

The final deployed model uses a **Random Forest Regressor** and is served through a **Streamlit web interface**.

---

## 📌 Project Overview

The project demonstrates:

- 🌲 Random Forest Regression to predict house prices (in dollars)
- 📊 Model evaluation using R² and MSE
- 🖥️ Interactive Streamlit web application
- 🚀 Deployment-ready ML project

---

## 📂 Project Structure

```
├── app.py                   # Streamlit application
├── model.pkl                # Trained Random Forest model
├── Prediction.ipynb         # Model training notebook
├── README.md                # Project documentation
```

---

## 📊 Dataset

**California Housing Dataset**  
Source: `sklearn.datasets.fetch_california_housing`  
Based on 1990 California Census data.

---

### 🔹 Features Used

| Feature   | Description                                      |
|-----------|--------------------------------------------------|
| MedInc    | Median income (in tens of thousands of dollars) |
| HouseAge  | Median age of houses                            |
| AveRooms  | Average number of rooms per household           |
| AveBedrms | Average number of bedrooms per household        |

---

### 🎯 Target Variable

| Variable | Description                      |
|----------|----------------------------------|
| PRICE    | Median house value in US dollars |

### Target Scaling

```python
df["PRICE"] = housing.target * 100000
```

---

## 🧠 Model Used

### 🌲 Random Forest Regressor

### Why Random Forest?

- Handles non-linear relationships
- More robust than Linear Regression
- Reduces overfitting via ensemble learning
- Performs well on structured/tabular data

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

### Evaluation Metrics

- **R² Score**
- **Mean Squared Error (MSE)**

Random Forest improves prediction performance compared to simple linear models by capturing complex feature interactions.

---

## 🖥️ Streamlit Web Application

### 🔹 Features

- User-friendly interface
- Median Income entered in **real dollars**
- Automatic conversion to dataset scale
- Real-time prediction output

### Example Scaling in App

```python
user_income = st.number_input("Median Income ($)", value=60000)
medinc = user_income / 10000
```

### Output

- 🏠 Predicted house price (USD)

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🛠️ Installation & Requirements

```bash
pip install numpy pandas scikit-learn streamlit
```

---

## ✅ Results & Insights

- Median Income is the most influential feature
- Random Forest provides strong predictive performance
- Model generalizes well with proper hyperparameter tuning

---

## 🚀 Future Improvements

- Add Latitude & Longitude features
- Add feature importance visualization in Streamlit
- SHAP explainability integration
- Try XGBoost or LightGBM
- Docker containerization for deployment

---

## 📜 License

This project is for educational and demonstration purposes.