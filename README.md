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

# Screenshots
## 1. Dataset Loading & Information
This section shows the dataset being loaded successfully and displays the dataset information, including the number of rows, columns, and data types.
**Screenshots**
<img width="1445" height="892" alt="Screenshot 2026-07-16 105909" src="https://github.com/user-attachments/assets/2f3f8119-8b4e-4f4c-bf0e-c5333f7a78c2" />
<img width="1515" height="900" alt="Screenshot 2026-07-16 110148" src="https://github.com/user-attachments/assets/f2936b11-d875-4f96-9454-cc68090a812e" />
<img width="1541" height="873" alt="Screenshot 2026-07-16 110241" src="https://github.com/user-attachments/assets/79b2bffe-4b6c-40c7-9d3a-a75158d1bf32" />





---
## 2. Data Preprocessing & Model Training
This section shows the preprocessing steps, feature encoding, model training, model evaluation, and saving the trained machine learning model.
**Screenshots**
<img width="1506" height="885" alt="Screenshot 2026-07-15 235919" src="https://github.com/user-attachments/assets/a505ccfd-3c79-4b39-b717-450b0cad3934" />

---

## 3. Prediction Using Trained Model
This section shows the prediction made by the trained model using sample student data.
**Screenshot**
<img width="908" height="120" alt="Screenshot 2026-07-16 000510" src="https://github.com/user-attachments/assets/24d7f266-b3d2-4fa7-a99a-fdb3811f54f4" />
---

## 4. Streamlit Web Application
This section shows the AI Student Performance Prediction web application developed using Streamlit, including the user input interface and the predicted final grade after clicking the **Predict** button.
**Screenshot**
<img width="917" height="828" alt="Screenshot 2026-07-16 101054" src="https://github.com/user-attachments/assets/f592297c-377e-48ac-a127-8d88ff4a0e63" />
<img width="893" height="865" alt="Screenshot 2026-07-16 101214" src="https://github.com/user-attachments/assets/37cb235c-dff0-44eb-8ff7-a7b9c62f6a7f" />
<img width="912" height="842" alt="Screenshot 2026-07-16 101140" src="https://github.com/user-attachments/assets/9b99d050-4538-4f3f-8590-b1aa74f491ed" />
<img width="947" height="852" alt="Screenshot 2026-07-16 101122" src="https://github.com/user-attachments/assets/a06773cc-fe6d-4354-9e9d-8973c4712f6f" />

---

## 5. GitHub Repository
This section shows the final project structure uploaded to GitHub with all required source code, model files, documentation, and project resources.

## Developed By

**Shivam Singh**

B.Tech (Computer Science & Engineering)

Ashoka Institute of Technology & Management

Dr. A.P.J. Abdul Kalam Technical University (AKTU)
