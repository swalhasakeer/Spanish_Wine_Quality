# 🍷 Spanish Wine Price Prediction

![image](https://github.com/user-attachments/assets/cb61a6f7-6627-472f-ba9f-752ebebcf156)


Predicting the price of Spanish red wines based on wine attributes like body, acidity, rating, and type using various machine learning models.

---

## 🥅 Goal of the Project

To analyze wine ratings, price variations, and customer preferences, and predict wine **price** from descriptive attributes using regression models.

---

## 📊 Dataset Description

This dataset contains **7,500+ Spanish red wines** with the following key attributes:

- `winery`, `wine`, `year`
- `rating`, `num_reviews`
- `region`, `type`
- `body`, `acidity`
- `price` (target variable)

It was collected using **web scraping** from multiple sources, including wine-specialized websites and supermarkets.

> 🔍 The dataset is ideal for **regression tasks** (predicting wine price) and includes **ordinal features** and **flavor-based metrics**.

---

## 🧪 Data Preprocessing Steps

- ✅ Outlier removal using **IQR method**
- ✅ Feature scaling with **StandardScaler**
- ✅ Skewness correction with **log1p transformation**
- ✅ Label encoding for categorical variables

---

## 📈 Model Performance

Multiple regression models were evaluated, including:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- **LGBM Regressor** ✅ (Best)

### 📌 Best Model: LGBM Regressor

| Metric | Score |
|--------|-------|
| MSE    | 0.2332 |
| MAE    | 0.3574 |
| R²     | 0.7717 ✅ |

> **LGBM Regressor** outperformed other models in all metrics, making it the most accurate for this task.

---

## 🖥️ Flask Web App

A Flask-based web application is included to **predict wine prices** using form inputs.  
Just input wine features like `rating`, `type`, `body`, etc., and get an instant price prediction.

![image](https://github.com/user-attachments/assets/ae55142f-fa6a-4f26-8f8e-32f24a88fefa) 

### Run the App Locally

   ```bash
   git clone https://github.com/swalhasakeer/WEATHER_AUS_EDA_SWALHA.git
   cd Rain\ Prediction
   pip install -r requirements.txt
   python app.py
   ```

## 🔧 Project Structure

```
├── Spanish_Wine_Quality_EDA.ipynb
├── app.py                  # Flask app
├── Scaler.pkl              # Standard Scaler
├── regression_model.pkl  # Trained model
├── templates/
│   └── form.html           # HTML form for user input               
├── requirements.txt
└── README.md
```

## 💡 Future Improvements
-  Add flavor-based NLP insights

-  Deploy using Render, Heroku, or AWS

-  Allow batch predictions via CSV
