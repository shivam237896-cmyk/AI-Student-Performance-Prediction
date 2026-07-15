import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


data = pd.read_csv("../data/student_data.csv")
print(data.head(5))

print(data.shape)
print(data.columns)
print(data.info())
print(data.describe())

x = data.drop("G3", axis=1)
y = data["G3"]

print("Features:")
print(x.head())

print("Target:")
print(y.head())
encoder = LabelEncoder()

encoder = LabelEncoder()

for column in x.select_dtypes(include=["object", "str"]).columns:
    x[column] = encoder.fit_transform(x[column])

print("Encoded Features:")
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print(x_train.shape)
print(x_test.shape)

model = RandomForestRegressor(random_state=42)
model.fit(x_train, y_train)

print("Model Trained Successfully")

predictions = model.predict(x_test)

from sklearn.metrics import mean_absolute_error, r2_score

print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

joblib.dump(model, "student_performance_model.pkl")
print("Model saved successfully")