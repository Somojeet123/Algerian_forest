import os
import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model and scaler
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "models", "ridgecv.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "models", "scaler.pkl"), "rb"))

@app.route("/", methods=["GET", "POST"])
def predict():

    prediction = None

    if request.method == "POST":
        try:
            Temperature = float(request.form["Temperature"])
            RH = float(request.form["RH"])
            Ws = float(request.form["Ws"])
            Rain = float(request.form["Rain"])
            FFMC = float(request.form["FFMC"])
            DMC = float(request.form["DMC"])
            ISI = float(request.form["ISI"])
            Classes = float(request.form["Classes"])
            Region = float(request.form["Region"])

            input_data = pd.DataFrame(
                [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]],
                columns=[
                    "Temperature",
                    "RH",
                    "Ws",
                    "Rain",
                    "FFMC",
                    "DMC",
                    "ISI",
                    "Classes",
                    "Region"
                ]
            )

            scaled_data = scaler.transform(input_data)
            prediction = model.predict(scaled_data)[0]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)