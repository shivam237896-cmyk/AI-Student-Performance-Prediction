# ==========================================================
# AI Student Performance Prediction Web Application
# Developed by: Shivam Singh
# ==========================================================

# Import required libraries
import streamlit as st
import joblib
import pandas as pd

# Load the trained machine learning model
model = joblib.load("models/student_performance_model.pkl")

# Title of the web application
st.title("🎓 AI Student Performance Prediction System")

# Small description
st.write("Enter the student's details below and click the Predict button.")

# Take input from the user
school = st.number_input("School (0 = GP, 1 = MS)", 0, 1, 0)
sex = st.number_input("Sex (0 = Female, 1 = Male)", 0, 1, 0)
age = st.number_input("Age", 15, 22, 18)
address = st.number_input("Address (0 = Rural, 1 = Urban)", 0, 1, 1)
famsize = st.number_input("Family Size", 0, 1, 0)
Pstatus = st.number_input("Parent Status", 0, 1, 0)
Medu = st.number_input("Mother Education", 0, 4, 4)
Fedu = st.number_input("Father Education", 0, 4, 4)
Mjob = st.number_input("Mother Job", 0, 4, 0)
Fjob = st.number_input("Father Job", 0, 4, 1)
reason = st.number_input("Reason", 0, 3, 0)
guardian = st.number_input("Guardian", 0, 2, 0)
traveltime = st.number_input("Travel Time", 1, 4, 2)
studytime = st.number_input("Study Time", 1, 4, 2)
failures = st.number_input("Failures", 0, 3, 0)
schoolsup = st.number_input("School Support", 0, 1, 1)
famsup = st.number_input("Family Support", 0, 1, 1)
paid = st.number_input("Paid Classes", 0, 1, 0)
activities = st.number_input("Extra Activities", 0, 1, 1)
nursery = st.number_input("Nursery", 0, 1, 1)
higher = st.number_input("Higher Education", 0, 1, 1)
internet = st.number_input("Internet Access", 0, 1, 1)
romantic = st.number_input("Romantic Relationship", 0, 1, 0)
famrel = st.number_input("Family Relationship", 1, 5, 4)
freetime = st.number_input("Free Time", 1, 5, 3)
goout = st.number_input("Going Out", 1, 5, 4)
Dalc = st.number_input("Workday Alcohol Consumption", 1, 5, 1)
Walc = st.number_input("Weekend Alcohol Consumption", 1, 5, 1)
health = st.number_input("Health", 1, 5, 3)
absences = st.number_input("Absences", 0, 100, 6)
G1 = st.number_input("First Period Grade (G1)", 0, 20, 5)
G2 = st.number_input("Second Period Grade (G2)", 0, 20, 6)

# Predict button
if st.button("Predict Final Grade"):

    # Create a DataFrame using user inputs
    sample = pd.DataFrame([{
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }])

    # Predict the final grade
    prediction = model.predict(sample)

    # Display the result
    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")