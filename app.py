
from flask import Flask, render_template_string, jsonify, request
import urllib.request, json, os

app = Flask(__name__)
API_KEY = "a6c7825a5ab54484927b5816d83fa087"

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/live")
def live():
    return jsonify({"message": "Live scores coming soon"})

@app.route("/past")
def past():
    finals = [
        {"year":"2022","home":"Argentina","away":"France","score":"3-3 (ARG pens)"},
        {"year":"2018","home":"France","away":"Croatia","score":"4-2"},
        {"year":"2014","home":"Germany","away":"Argentina","score":"1-0"},
    ]
    return jsonify(finals)

@app.route("/ai_predict")
def ai_predict():
    home = request.args.get("home","Team A")
    away = request.args.get("away","Team B")
    return jsonify({"prediction": f"Based on recent form, {home} are slight favourites. Their home record and attacking strength gives them the edge. Predicted score: {home} 2-1 {away}."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
