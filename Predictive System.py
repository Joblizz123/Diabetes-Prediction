# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# Loading the saved model

with open('C:/Users/Joe Solomon/Deploying ML Models/diabetes_saved_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
 
    
input_data = (4, 112, 67, 28, 0, 15.6, 0.4, 19)
input_data_array = np.array(input_data)

# Reshape the array since we are predicting for one instance
input_data_array = input_data_array.reshape(1, -1)

prediction = loaded_model.predict(input_data_array)
print(prediction)

if prediction == 1:  
    print('The patient has diabetes, please administer the treatment')
else:
    print('The patient has no diabetes, good to go!')