from fastapi import FastAPI
from pydantic import BaseModel 
import pickle
import json


app = FastAPI()
class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.dict()
    preg = input_data['Pregnancies']
    glu = input_data['Glucose']
    bp = input_data['BloodPressure']
    st = input_data['SkinThickness']
    ins = input_data['Insulin']
    bmi = input_data['BMI']
    dpf = input_data['DiabetesPedigreeFunction']
    age = input_data['Age']

    input_data = [[preg, glu, bp, st, ins, bmi, dpf, age]]
    prediction = diabetes_model.predict(input_data)
    if prediction[0] == 0:
        return {'prediction': 'No Diabetes'}
    else:
        return {'prediction': 'Diabetes'}
