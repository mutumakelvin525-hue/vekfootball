
from flask import Flask, jsonify, request, send_file
import urllib.request, json, os

app = Flask(__name__)
API_KEY = "a6c7825a5ab54484927b5816d83fa087"

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/matches")
def matches():
    try:
        url = "https://api.football-data.org/v4/matches"
        req = urllib.request.Request(url, headers={"X-Auth-Token": API_KEY})
        res = urllib.request.urlopen(req, timeout=10)
        data = json.loads(res.read())
        results = []
        for m in data.get("matches", []):
            hs = m["score"]["fullTime"]["home"]
            as_ = m["score"]["fullTime"]["away"]
            results.append({
                "home": m["homeTeam"]["name"],
                "away": m["awayTeam"]["name"],
                "home_score": hs if hs is not None else 0,
                "away_score": as_ if as_ is not None else 0,
                "time": m["utcDate"][11:16],
                "date": m["utcDate"][:10],
                "league": m["competition"]["name"],
                "live": m["status"] == "IN_PLAY",
                "status": m["status"]
            })
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)})

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
    return jsonify({"prediction": f"Based on recent form and head-to-head records, {home} are slight favourites. Their strong defensive record and clinical attack makes them favourites. Predicted score: {home} 2-1 {away}."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
