# Machine Learning Repository

Welcome to the **Machine Learning Repository**, a collection of ML algorithms, implementations, and projects from **basic to advanced levels**. 
This repository serves as a reference for ML concepts, covering supervised, unsupervised, and deep learning techniques.

---


---

##  Basics of Machine Learning
The fundamental ML algorithms include:
- **Linear Regression** → Predict continuous values 📈
- **Logistic Regression** → Binary classification 🔴🔵
- **K-Nearest Neighbors (KNN)** → Distance-based classification 🤖
- **Decision Trees** → Rule-based classification 🌳

Example Code for **Linear Regression**:
```python
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load dataset
df = pd.read_csv('House_Prices.csv')
# --> convert to dataframes

X = df[['Size', 'Bedrooms']]  # X = feature variables
y = df['Price'] #y = output / target variable 


# Train model
model = LinearRegression()
model.fit(X, y)
 
# Prediction
predicted_price = model.predict([[2500, 3]])
print(f"Predicted Price: ${predicted_price[0]:.2f}")
