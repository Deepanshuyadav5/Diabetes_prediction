# Testing the model 
import json 
import requests

url = 'http://localhost:8000/diabetes_prediction'

input_data = {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}
response = requests.post(url, json=input_data)

print(response.text)