import joblib
import pandas as pd

model = joblib.load("../models/student_performance_model.pkl")
print("Model Loaded Successfully")

sample = [[
    0, 0, 18, 1, 0, 0, 4, 4, 0, 1, 0, 0,
    2, 2, 0, 1, 1, 0, 1, 1, 1, 1, 0,
    4, 3, 4, 1, 1, 3, 6, 5, 6
]]

prediction = model.predict(sample)

print("Predicted Final Grade (G3):", prediction[0])