from os import cpu_count

from flask.templating import render_template
from app.main.util.apiresponse import apiResponse
from flask import request
import numpy as np
import json
import joblib
import dill
from sklearn.feature_extraction.text import TfidfVectorizer

async def conv_chars(word):
    chars = []
    for letter in word:
        chars.append(letter)
    return chars
 
vectorizer = dill.load(open("./artifacts/vectorizer.pkl", 'rb'))
     
def load_saved_artifacts():
    with open("./artifacts/pred_dictionary.json", 'r') as f:
        pred_dict = json.load(f)

    with open("./artifacts/xgbclassifier.pkl", 'rb') as f:
        model = joblib.load(f)

    return pred_dict, model

def passwordstrengthpredict(data):
    try:

        password = data['password']
        
        pred_dict, model = load_saved_artifacts()  
        
        x = vectorizer.transform([password])
        
        y = model.predict(x)
        
        
        return apiResponse(True, f'Password is {pred_dict[f"{str(y[0])}"]}', str(y[0]), None), 200
        

    except Exception as e:
        return apiResponse(False, 'Error Occurred', None, str(e)), 500
