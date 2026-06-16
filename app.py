from flask import Flask, render_template, request, jsonify
import joblib
import logging

app = Flask(__name__)

model = joblib.load("model.pkl")

flowers = [
    "Setosa",
    "Versicolor",
    "Virginica"
]

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    sl=float(request.form["sl"])
    sw=float(request.form["sw"])
    pl=float(request.form["pl"])
    pw=float(request.form["pw"])

    prediction=model.predict([[sl,sw,pl,pw]])

    result=flowers[prediction[0]]

    logging.info(
        f"Website Prediction: {result}"
    )

    return render_template(
        "index.html",
        prediction=result
    )

@app.route("/api/predict", methods=["POST"])
def api_predict():

    data=request.get_json()

    prediction=model.predict([[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]])

    result=flowers[prediction[0]]

    logging.info(
        f"API Prediction: {result}"
    )

    return jsonify({
        "prediction": result
    })

if __name__=="__main__":
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)