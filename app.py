
from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():

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

    output = round(prediction[0])
    
    if output == 0:
        response = jsonify({'label': 0})
    else:
        response = jsonify({'label': 1})
         
    return response

        

if __name__ == "__main__":
    app.run(debug=True)
