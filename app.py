
from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import sklearn
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Flask Machine Learning based Diabetes prediction API</h1>"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    """
    pregnancy = float(request.form["pregnancy"])

    glucose = int(request.form['glucose'])

    bloodpressure = float(request.form["bloodpressure"])

    thickness = float(request.form["thickness"])

    insulin = float(request.form["insulin"])

    bmi = float(request.form["bmi"])

    pedigree = float(request.form["pedigree"])

    age = int(request.form["age"])

    prediction = model.predict([[
        pregnancy,
        glucose,
        bloodpressure,
        thickness,
        insulin,
        bmi,
        pedigree,
        age
    ]])
    """
    
    prediction = model.predict([[float(request.args['age']),
                            float(request.args['gender']),
                            float(request.args['polyuria']),
                            float(request.args['polydipsia']),
                            float(request.args['weakness']),
                            float(request.args['visual']),
                            float(request.args['healing']),
                            float(request.args['partial']),
                            float(request.args['muscle']),
                            float(request.args['alopecia'])
                           ]])

    output = round(prediction[0])
    
    if output == 0:
        response = jsonify({'label': 0})
    else:
        response = jsonify({'label': 1})
        
    response.headers.add('Access-Control-Allow-Origin', '*')
         
    return response

@app.route("/androidpredict", methods=["GET", "POST"])
def androidpredict():
    
    prediction = model.predict([[float(request.form['age']),
                            float(request.form['gender']),
                            float(request.form['polyuria']),
                            float(request.form['polydipsia']),
                            float(request.form['weakness']),
                            float(request.form['visual']),
                            float(request.form['healing']),
                            float(request.form['partial']),
                            float(request.form['muscle']),
                            float(request.form['alopecia'])
                           ]])

    output = round(prediction[0])
    
    if output == 0:
        return "No"
    else:
        return "Yes"


if __name__ == "__main__":
    app.run(debug=True)
"""

import flask
from flask import request, render_template, jsonify
from flask_cors import CORS
import pickle

app = flask.Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return '<h1>API is working.. </h1>'


@app.route('/predict',methods=['GET','POST'])
def predict():
    prediction = model.predict([[float(request.args['pregnancy']),
                            float(request.args['glucose']),
                            float(request.args['bloodpressure']),
                            float(request.args['thickness']),
                            float(request.args['insulin']),
                            float(request.args['bmi']),
                            float(request.args['pedigree']),
                            float(request.args['age'])
                           ]])
         
    return str(round(prediction[0]))


if __name__ == "__main__":
    app.run(debug=True)
"""
