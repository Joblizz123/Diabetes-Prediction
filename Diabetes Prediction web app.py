# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 04:44:45 2023

@author: Joe Solomon
"""

import numpy as np
import pickle
import streamlit as st

# Loading the model
with open('C:/Users/Joe Solomon/Deploying ML Models/diabetes_saved_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)


def diabetes_prediction(input_data):
    # Changing the input data to array
    input_data_array = np.array(input_data)

    # Reshape the array since we are predicting for one instance
    input_data_array = input_data_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_array)
    print(prediction)

    if prediction == 1:  
        return 'The patient has diabetes, please administer the treatment'
    else:
        return 'The patient has no diabetes, good to go!'



def main():
    
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    # getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnacies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age')
    
    # Code for prediction
    diagnosis = ''
    
    # Code for button
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()