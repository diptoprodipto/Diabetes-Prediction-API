
from flask import Flask, request, render_template, jsonify
#from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
@app.route("/home")
# @cross_origin()
def home():
    return render_template("index.html")


@app.route("/test")
# @cross_origin()
def test():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":

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

        """
        if output == 0:
            ans = "You don't have Heart Disease"
        else:
            ans = "You have Heart Disease"

        return render_template('index.html',prediction_text="{}".format(ans))
        """
        if output == 0:
            return jsonify({prediction:[{"label": 0}])
        else:
            return jsonify({prediction:[{"label": 1}])

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
