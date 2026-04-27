# 🏠 Bengaluru House Price Predictor

🚀 **Live Demo:** [Click here to use the App](https://bengaluru-house-pricing-8vzq5dusmpbjmi58vqezgj.streamlit.app/)

## 📌 Project Overview
This is a Full-Stack Machine Learning project that predicts real estate prices in Bengaluru, India. Predicting house prices is a classic regression problem, but this project goes a step further by providing an interactive UI for users to get instant estimates.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python-based web framework)
* **Machine Learning:** Scikit-Learn (Linear Regression & Ridge Regression)
* **Data Manipulation:** Pandas & NumPy
* **Visualization:** Matplotlib & Seaborn
* **Deployment:** Streamlit Community Cloud

## 📊 Dataset & Preprocessing
The dataset used is the "Bengaluru House Price Data" from Kaggle.
* **Data Cleaning:** Handled missing values and removed outliers in `Total_sqft`, `BHK`, and `Price_per_sqft`.
* **Feature Engineering:** Used **One-Hot Encoding** for locations and consolidated locations with fewer than 10 data points into an "Other" category to reduce dimensionality.
* **Outlier Removal:** Applied business logic (e.g., BHK vs Sqft ratio) and Standard Deviation filtering to remove anomalies.

## 🤖 The Model
After testing multiple algorithms (Linear Regression, Lasso, and Ridge), the **Ridge Regression** model was selected for its ability to prevent overfitting through L2 regularization.

## 🚀 How to Run Locally
1. Clone the repo: `git clone https://github.com/gaurav25bm/Bengaluru-House-Pricing.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

---
*Created by Gaurav Anand B M*
