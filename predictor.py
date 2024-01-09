import numpy as np
import pandas as pd
import pickle

loaded_model = pickle.load(open("C:/Users/Harshali Vadher/Desktop/EDT/CHDpredMod.sav"),'rb')
input_data = ()
input_data_array = np.asarray(input_data)
data_reshaped = input_data_array.reshape(1,-1)
prediction = loaded_model.predict(data_reshaped)

if prediction[0]==0:
    print('LESS risk of coronary heart disease')
else:
    print('HIGH risk of coronory heart disearse')

