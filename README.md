# Diabetes-Prediction
### INTRODUCTION
This  is a binary classification problem focused on predicting the cases of diabetes.

The dataset was sourced from kaggle. It consists of about 768 recoreds and nine features. This is a rather biased project as it only considered women, evident in the pregnancies feature. It is actually a simple machine learning project. The features are the number of pregnancies, glucose level, blood pressure, skin  thickness, insulin level in the body, the Body Mass Index (BMI), the diabetes pedigree function, the age and ofcourse the outcome.
### EDA & VISUALIZATIONS
Analysis were performed on the dataset. Missing values and duplicates were checked. As part of the Exploratory Data Analysis, a few visualizations to better understand the data were alos performed. From the visualizations, there is no noticeable relationahip between the Age of patients and Blood Pressure. Seaborn's FacetGrid was employed to visualize the distribution of each of the features. I also checked the correlation of the feaures, and visualized them using Seaborn's heatmap method. No feature was significantly correlated, suggesting that all the features can be usied for model building.

### MODELLING PHASE/ MODEL BUILDING
The dataset was split into the training and testing sets using scit-kit learn's train_test_split. Ofcourse the data needs to be sclaed  in order to have a uniform vector system, that is, mean of 0 and standard deviation of 1.

I tried to use hyperparameter tuning, considering Logistic Regression, Support Vector Classifier (SVC), and Random Forest Classifier. The SVC performed best with training and test accuracy score of 79.5% and 75.3% respectively. The model was saved and deployed using Streamlit.
