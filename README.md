# AI Student Performance Prediction

## Project Description
The AI Student Performance Prediction project is a Machine Learning application that predicts a student's final academic grade (G3) based on various factors such as age, study time, previous grades, family background, health, absences, and other student-related information.

The project uses a Random Forest Regressor model, which is trained on a student performance dataset. After training, the model is saved and later loaded to predict the final grade of a student using new input data.

---

## Objectives

- Predict the final student grade (G3).
- Apply Machine Learning to educational data.
- Learn data preprocessing and feature encoding.
- Train and evaluate a regression model.
- Save and reuse the trained model.

## Dataset

The dataset used in this project was downloaded from Kaggle.

**Source:** Student Performance Prediction Dataset

**Link:** https://www.kaggle.com/datasets/devansodariya/student-performance-data

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Visual Studio Code

---

## Project Structure

```
AI-Student-Performance-Prediction/
│
├── data/
│   └── student_data.csv
│
├── models/
│   └── student_performance_model.pkl
│
├── src/
│   ├── train_model.py
│   └── predict.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Workflow

1. Load the student dataset.
2. Display dataset information.
3. Separate features and target.
4. Encode categorical columns.
5. Split the dataset into training and testing sets.
6. Train the Random Forest Regressor model.
7. Evaluate the model using MAE and R² Score.
8. Save the trained model.
9. Load the saved model.
10. Predict the student's final grade.

---

## Model Performance

- Algorithm: Random Forest Regressor
- Evaluation Metric: Mean Absolute Error (MAE)
- Evaluation Metric: R² Score

The trained model successfully predicts the final student grade based on the given input features.

---

## Sample Output

```
Model Trained Successfully
MAE: 1.10
R2 Score: 0.83
Model Saved Successfully

Model Loaded Successfully
Predicted Final Grade (G3): 6.26
```

---

## Future Improvements

- Build a graphical user interface (GUI).
- Create a web application using Flask or Streamlit.
- Improve prediction accuracy by testing different Machine Learning algorithms.
- Deploy the model online for public use.

---
# 📸 Output Screenshots

## 1. Dataset Preview
data.head()

## 2. Dataset Shape
data.shape

## 3. Dataset Columns
data.columns

## 4. Dataset Information
data.info()

## 5. Statistical Summary
data.describe()

## 6. Features (X)
print(x.head())

## 7. Target Variable (Y)
print(y.head())

## 8. Encoded Features
Encoded Features

## 9. Training and Testing Data Split
x_train.shape and x_test.shape

## 10. Model Training
Model Trained Successfully

## 11. Model Evaluation
MAE and R² Score

## 12. Model Saving
Model Saved Successfully

## 13. Model Loading
Model Loaded Successfully

## 14. Prediction Output
Predicted Final Grade (G3): 6.26

## Developed By

**Shivam Singh**

B.Tech (Computer Science & Engineering)

Ashoka Institute of Technology & Management

Dr. A.P.J. Abdul Kalam Technical University (AKTU)