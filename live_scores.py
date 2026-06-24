import urllib.request
import json

API_KEY = "a6c7825a5ab54484927b5816d83fa087"

def run():
    print("\n=== Live & Upcoming World Cup Matches ===")
    try:
        for status in ["LIVE", "SCHEDULED"]:
            url = f"https://api.football-data.org/v4/competitions/WC/matches?status={status}"
            req = urllib.request.Request(url, headers={"X-Auth-Token": API_KEY})
            res = urllib.request.urlopen(req)
            data = json.loads(res.read())
            matches = data["matches"][:5]
            if matches:
                print(f"\n-- {status} --")
                for m in matches:
                    home = m["homeTeam"]["name"]
                    away = m["awayTeam"]["name"]
                    date = m["utcDate"][:10]
                    score = m["score"]["fullTime"]
                    print(f"{date} | {home} {score['home']} - {score['away']} {away}")
    except Exception as e:
        print(f"Error: {e}")
