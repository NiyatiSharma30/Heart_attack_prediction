import streamlit as st
import pickle
import numpy as np

with open  ('C:/Users/91703/Downloads/logreg_pickle', 'rb') as file:
    model = pickle.load(file)


# Create the title and intro
st.title("Heart Attack Prediction")
st.write("Input the patient's information to predict the risk of a heart attack")

# Get input from the user
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex (0: Female, 1: Male)", options=[0, 1])
cp = st.selectbox("Chest Pain Type (0-3)", options=[0, 1, 2, 3])
trtbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=500, value=200)
fbs = st.selectbox("Fasting Blood Sugar (0: <120mg/dl, 1: >120mg/dl)", options=[0, 1])
restecg = st.selectbox("Resting ECG Results (0-2)", options=[0, 1, 2])
thalachh = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
exng = st.selectbox("Exercise Induced Angina (0: No, 1: Yes)", options=[0, 1])
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
slp = st.selectbox("Slope of the Peak Exercise ST Segment (0-2)", options=[0, 1, 2])
caa = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4, value=0)
thall = st.selectbox("Thalassemia (1-3)", options=[1, 2, 3])

# Prepare the input data for prediction
input_data = np.array([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])

# Make the prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Prediction (0: No heart attack, 1: Heart attack):", int(prediction[0]))
