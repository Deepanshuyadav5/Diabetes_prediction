import streamlit as st
import requests
import json

st.title("Diabetes Prediction")
st.markdown("### Check diabetes status using ML")
st.sidebar.header("User Input")

def get_user_input():
    pregnancies = st.sidebar.number_input("Pregnancies", 0, 17, 3)
    glucose = st.sidebar.number_input("Glucose", 0, 200, 120)
    blood_pressure = st.sidebar.number_input("Blood Pressure", 0, 120, 80)
    skin_thickness = st.sidebar.number_input("Skin Thickness", 0, 100, 20)
    insulin = st.sidebar.number_input("Insulin", 0, 500, 80)
    bmi = st.sidebar.number_input("BMI", 0.0, 60.0, 25.0)
    diabetes_pedigree_function = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 2.0, 0.5)
    age = st.sidebar.number_input("Age", 0, 100, 30)

    user_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree_function,
        "Age": age
    }
    return user_data


user_data = get_user_input()

st.subheader("Your Input Summary")
col1, col2 = st.columns(2)
with col1:
    st.write(f"**Pregnancies:** {user_data['Pregnancies']}")
    st.write(f"**Glucose:** {user_data['Glucose']}")
    st.write(f"**Blood Pressure:** {user_data['BloodPressure']}")
    st.write(f"**Skin Thickness:** {user_data['SkinThickness']}")
with col2:
    st.write(f"**Insulin:** {user_data['Insulin']}")
    st.write(f"**BMI:** {user_data['BMI']}")
    st.write(f"**Diabetes Pedigree Function:** {user_data['DiabetesPedigreeFunction']}")
    st.write(f"**Age:** {user_data['Age']}")

st.markdown("---")

# Predict button
if st.button("Predict"):
    try:
        response = requests.post(
            "http://localhost:8000/diabetes_prediction",
            json=user_data
        )
        result = response.json()

        if result["prediction"] == "No Diabetes":
            st.success("✅ Result: **No Diabetes** — The person is not diabetic.")
        else:
            st.error("⚠️ Result: **Diabetes** — The person is likely diabetic.")

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the API. Make sure the FastAPI server is running on port 8000.\n\nRun: `uvicorn main:app --reload`")
