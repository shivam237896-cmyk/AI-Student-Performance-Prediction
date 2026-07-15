import joblib
import pandas as pd

model = joblib.load("../models/student_performance_model.pkl")
print("Model Loaded Successfully")

columns = [
    "school", "sex", "age", "address", "famsize", "Pstatus",
    "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
    "traveltime", "studytime", "failures", "schoolsup",
    "famsup", "paid", "activities", "nursery", "higher",
    "internet", "romantic", "famrel", "freetime", "goout",
    "Dalc", "Walc", "health", "absences", "G1", "G2"
]

sample = pd.DataFrame([[
    0, 0, 18, 1, 0, 0,
    4, 4, 0, 1, 0, 0,
    2, 2, 0, 1, 1, 0,
    1, 1, 1, 1, 0,
    4, 3, 4, 1, 1, 3,
    6, 5, 6
]], columns=columns)

prediction = model.predict(sample)

print("Predicted Final Grade (G3):", prediction[0])