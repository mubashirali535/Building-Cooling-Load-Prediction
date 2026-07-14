# 1. Import Libraries
import pandas as pd
import numpy as np

# 2. Load Dataset
df = pd.read_csv("energy_efficiency_data.csv")

# 3. Display dataset information
print(df.head())

print(df.info())

print(df.describe())

# 4. Check for missing values and duplicate records
print(df.isnull().sum())

print(df.duplicated().sum())

# 5. Visualize the correlation for features selection
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# 6. Select input features and target variable
y = df["Cooling_Load"]
X = df[
    [
        "Relative_Compactness",
        "Surface_Area",
        "Wall_Area",
        "Roof_Area",
        "Overall_Height",
        "Glazing_Area"
    ]
]

# 7. Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Train machine learning models
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(random_state = 42)
dt.fit(X_train, y_train)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state = 42)
rf.fit(X_train, y_train)

# 9. Make predictions using trained models
pred_lr=lr.predict(X_test)
pred_dt=dt.predict(X_test)
pred_rf=rf.predict(X_test)

# 10. Evaluate model performance
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

results = pd.DataFrame({
    "Model": ["Linear Regression", "Decision Tree", "Random Forest"],
    "MAE": [
        mean_absolute_error(y_test, pred_lr),
        mean_absolute_error(y_test, pred_dt),
        mean_absolute_error(y_test, pred_rf)
    ],
    "MSE": [
        mean_squared_error(y_test, pred_lr),
        mean_squared_error(y_test, pred_dt),
        mean_squared_error(y_test, pred_rf)
    ],
    "RMSE": [
        np.sqrt(mean_squared_error(y_test, pred_lr)),
        np.sqrt(mean_squared_error(y_test, pred_dt)),
        np.sqrt(mean_squared_error(y_test, pred_rf))
    ],
    "R2 Score": [
        r2_score(y_test, pred_lr),
        r2_score(y_test, pred_dt),
        r2_score(y_test, pred_rf)
    ],

})

print(results)

# 11. Save the best-performing model
import joblib
joblib.dump(dt, "decision_tree_cooling_model.pkl")