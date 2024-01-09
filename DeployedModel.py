import numpy as np
import pickle
import streamlit as slit

loaded_model = pickle.load(open('C:/Users/Harshali Vadher/Desktop/EDT/CHDpredMod.sav','rb'))

def CHD_prediction(input_data):
    #input_data = ()

    input_data_array = np.asarray(input_data)
    data_reshaped = input_data_array.reshape(1,-1)
    prediction = loaded_model.predict(data_reshaped)

    if prediction[0]==0:
        return 'LESS risk of coronary heart disease' 
    else:
        return 'HIGH risk of coronory heart disearse precautions to take: https://www.nhs.uk/conditions/coronary-heart-disease/prevention/'

def main():
    slit.title('Coronary Heart Disease Predictor')
    male = slit.selectbox('what is your gender',('Male','Female'))

    if male ==  'Male':
        male = 1
    else:
        male = 0

    age = slit.number_input('what is your age',format='%d',value=0)

    currentSmoker = slit.selectbox('Do you smoke?',(' ','Yes','No'))

    if currentSmoker == 'Yes':
        currentSmoker = 1
        cigsPerDay = 0
        cigsPerDay = slit.number_input('How many cigarettes per day?',format='%d',value=0)
    else:
        currentSmoker = 0
        cigsPerDay = 0
        
    BPMeds = slit.selectbox('Do you take meds for BP',(' ','Yes','No'))

    if BPMeds == 'Yes':
        BPMeds = 1
    else:
        BPMeds = 0

    prevalentStroke = slit.selectbox('did you have a prev incident of stroke',(' ','Yes','No'))

    if prevalentStroke == 'Yes':
        prevalentStroke = 1
    else:
        prevalentStroke = 0

    prevalentHyp = slit.selectbox('Do you have past reports of Hyptertension',(' ','Yes','No'))

    if prevalentHyp == 'Yes':
        prevalentHyp = 1
    else:
        prevalentHyp = 0

    diabetes = slit.selectbox('Do you suffer from diabeties',(' ','Yes','No'))

    if diabetes == 'Yes':
        diabetes = 1
    else:
        diabetes = 0
        
    totChol = slit.number_input('what is your total cholestrol')
    sysBP = slit.number_input('what is your systolic blood pressure')
    diaBP = slit.number_input('what is your diastolic blood pressure')
    heartRate = slit.number_input('what is your heart rate')
    BMI = slit.number_input('what is your BMI')
    glucose = slit.number_input('what are your glucose level')

    diagonosis = ''

    if slit.button('CHD Test Result '):
        diagonosis = CHD_prediction([male,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose])
    slit.success(diagonosis)

if __name__ == '__main__':
    main()