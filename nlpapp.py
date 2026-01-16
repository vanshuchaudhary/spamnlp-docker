from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("spam.pkl")

@app.route("/",methods = ["get"])
def home():
    return "NLP BASED SPAM DETECTION APP"

@app.route("/message", methods=["GET"])
def message():
    return "Use POST /predict in Postman to classify messages"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message", "").strip()

    if message == "":
        return jsonify({"error": "Please enter a message"}), 400

    proba = model.predict_proba([message])[0][1]
    prediction = 1 if proba > 0.35 else 0

    result = "SPAM" if prediction == 1 else "HAM"

    return jsonify({
        "message": message,
        "spam_probability": round(proba, 3),
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True,port = 8000,host = "0.0.0.0")
