from flask import Flask, render_template_string, jsonify
import urllib.request
import json

app = Flask(__name__)
API_KEY = "a6c7825a5ab54484927b5816d83fa087"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>World Cup Analyzer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial; background: #1a1a2e; color: white; margin: 0; padding: 10px; }
        h1 { color: #e94560; text-align: center; }
        .btn { background: #e94560; color: white; border: none; padding: 10px 20px; margin: 5px; border-radius: 8px; cursor: pointer; width: 100%; font-size: 16px; }
        .card { background: #16213e; padding: 15px; border-radius: 10px; margin: 10px 0; }
        #result { margin-top: 20px; }
        select { width: 100%; padding: 10px; margin: 5px 0; border-radius: 8px; background: #16213e; color: white; border: 1px solid #e94560; }
    </style>
</head>
<body>
    <h1>⚽ World Cup Analyzer</h1>

    <div class="card">
        <button class="btn" onclick="fetch('/live').then(r=>r.json()).then(d=>show(d))">🔴 Live Scores</button>
        <button class="btn" onclick="fetch('/past').then(r=>r.json()).then(d=>show(d))">📊 Past Finals</button>
    </div>

    <div class="card">
        <h3>🔮 Predict Match</h3>
        <select id="home"><option>Select Home Team</option></select>
        <select id="away"><option>Select Away Team</option></select>
        <button class="btn" onclick="predict()">Predict!</button>
    </div>

    <div class="card">
        <h3>👤 Compare Players</h3>
        <select id="p1"><option>Select Player 1</option></select>
        <select id="p2"><option>Select Player 2</option></select>
        <button class="btn" onclick="compare()">Compare!</button>
    </div>

    <div id="result" class="card"></div>

    <script>
        const teams = ["Brazil","France","Argentina","England","Germany","Spain","Portugal","Netherlands"];
        const players = ["Messi","Ronaldo","Mbappe","Neymar","Haaland","Benzema","Salah","Lewandowski"];

        teams.forEach(t => {
            document.getElementById("home").innerHTML += `<option>${t}</option>`;
            document.getElementById("away").innerHTML += `<option>${t}</option>`;
        });
        players.forEach(p => {
            document.getElementById("p1").innerHTML += `<option>${p}</option>`;
            document.getElementById("p2").innerHTML += `<option>${p}</option>`;
        });

        function show(data) {
            document.getElementById("result").innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
        }

        function predict() {
            const h = document.getElementById("home").value;
            const a = document.getElementById("away").value;
            fetch(`/predict?home=${h}&away=${a}`).then(r=>r.json()).then(d=>show(d));
        }

        function compare() {
            const p1 = document.getElementById("p1").value;
            const p2 = document.getElementById("p2").value;
            fetch(`/compare?p1=${p1}&p2=${p2}`).then(r=>r.json()).then(d=>show(d));
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/live")
def live():
    try:
        results = []
        for status in ["LIVE", "SCHEDULED"]:
            url = f"https://api.football-data.org/v4/competitions/WC/matches?status={status}"
            req = urllib.request.Request(url, headers={"X-Auth-Token": API_KEY})
            res = urllib.request.urlopen(req)
            data = json.loads(res.read())
            for m in data["matches"][:3]:
                results.append({
                    "home": m["homeTeam"]["name"],
                    "away": m["awayTeam"]["name"],
                    "date": m["utcDate"][:10],
                    "status": status
                })
        return jsonify(results if results else {"message": "No matches right now"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/past")
def past():
    finals = [
        {"year": "2022", "home": "Argentina", "away": "France", "score": "3-3 (ARG pens)", "venue": "Qatar"},
        {"year": "2018", "home": "France", "away": "Croatia", "score": "4-2", "venue": "Russia"},
        {"year": "2014", "home": "Germany", "away": "Argentina", "score": "1-0", "venue": "Brazil"},
        {"year": "2010", "home": "Spain", "away": "Netherlands", "score": "1-0", "venue": "South Africa"},
        {"year": "2006", "home": "Italy", "away": "France", "score": "1-1 (ITA pens)", "venue": "Germany"},
    ]
    return jsonify(finals)

@app.route("/predict")
def predict():
    from flask import request
    ratings = {"Brazil":88,"France":87,"Argentina":87,"England":85,"Germany":84,"Spain":85,"Portugal":84,"Netherlands":83}
    attack = {"Brazil":90,"France":89,"Argentina":91,"England":86,"Germany":85,"Spain":87,"Portugal":88,"Netherlands":84}
    h = request.args.get("home")
    a = request.args.get("away")
    if h not in ratings or a not in ratings:
        return jsonify({"error": "Invalid teams"})
    hs = (ratings[h] + attack[h]) / 2 + 3
    as_ = (ratings[a] + attack[a]) / 2
    if hs > as_ + 3:
        winner = h
    elif as_ > hs:
        winner = a
    else:
        winner = "Draw"
    return jsonify({"home": h, "away": a, "prediction": winner, "home_strength": round(hs,1), "away_strength": round(as_,1)})

@app.route("/compare")
def compare():
    from flask import request
    data = {
        "Messi": {"goals":98,"assists":56,"wc_goals":13,"speed":85,"dribbling":96},
        "Ronaldo": {"goals":128,"assists":41,"wc_goals":8,"speed":87,"dribbling":89},
        "Mbappe": {"goals":48,"assists":38,"wc_goals":12,"speed":97,"dribbling":92},
        "Neymar": {"goals":79,"assists":56,"wc_goals":8,"speed":90,"dribbling":94},
        "Haaland": {"goals":75,"assists":30,"wc_goals":0,"speed":89,"dribbling":80},
        "Benzema": {"goals":77,"assists":58,"wc_goals":8,"speed":78,"dribbling":87},
        "Salah": {"goals":71,"assists":45,"wc_goals":2,"speed":91,"dribbling":90},
        "Lewandowski": {"goals":82,"assists":57,"wc_goals":10,"speed":78,"dribbling":82},
    }
    p1 = request.args.get("p1")
    p2 = request.args.get("p2")
    if p1 not in data or p2 not in data:
        return jsonify({"error": "Invalid players"})
    return jsonify({"player1": {p1: data[p1]}, "player2": {p2: data[p2]}})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
