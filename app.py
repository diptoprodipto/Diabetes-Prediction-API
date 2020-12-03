
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Flask Machine Learning based Diabetes prediction API</h1>"

@app.route("/predict", methods=["GET", "POST"])
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
        
    response.headers.add('Access-Control-Allow-Origin', '*')
         
    return response


if __name__ == "__main__":
    app.run(debug=True)
