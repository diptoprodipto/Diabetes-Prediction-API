from warnings import catch_warnings
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
    return jsonify({
        "about": "This is a Flask REST API for predicting diabetes",
        "written_by": "Prodipto Roy Dipto",
        "method": "GET/POST",
        "query_params": {
            "age": "number",
            "gender": "1/0",
            "polyuria": "1/0",
            "polydipsia": "1/0",
            "sudden": "1/0",
            "itching": "1/0",
            "irritability": "1/0",
            "delayed": "1/0",
            "partial": "1/0",
            "alopecia": "1/0"
        }
    })

@app.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        # pregnancy = float(request.form["pregnancy"])
        # glucose = int(request.form['glucose'])
        # response.headers.add('Access-Control-Allow-Origin', '*')

        prediction = model.predict([[float(request.args['age']),
                                float(request.args['gender']),
                                float(request.args['polyuria']),
                                float(request.args['polydipsia']),
                                float(request.args['sudden']),
                                float(request.args['itching']),
                                float(request.args['irritability']),
                                float(request.args['delayed']),
                                float(request.args['partial']),
                                float(request.args['alopecia'])
                            ]])

        output = round(prediction[0])
    
        if output == 0:
            return jsonify({'label': 0})
        else:
            return jsonify({'label': 1})
    except Exception:
        return jsonify({
                "message": "Not enough or wrong type of data provided!"
            })

@app.route("/androidpredict", methods=["GET", "POST"])
def androidpredict():
    try:
        prediction = model.predict([[float(request.form['age']),
                                float(request.form['gender']),
                                float(request.form['polyuria']),
                                float(request.form['polydipsia']),
                                float(request.form['sudden']),
                                float(request.form['itching']),
                                float(request.form['irritability']),
                                float(request.form['delayed']),
                                float(request.form['partial']),
                                float(request.form['alopecia'])
                            ]])

        output = round(prediction[0])
        
        if output == 0:
            return "No"
        else:
            return "Yes"
    except Exception:
        return jsonify({
                "message": "Not enough or wrong type of data provided!"
            })

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
