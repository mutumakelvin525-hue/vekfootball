import live_scores
import past_stats
import predictor
import players

def menu():
    print("\n=== World Cup Analyzer ===")
    print("1. Live Scores")
    print("2. Past Stats")
    print("3. Predict Match")
    print("4. Compare Players")
    print("5. Exit")
    return input("Choose: ")

while True:
    c = menu()
    if c == "1": live_scores.run()
    elif c == "2": past_stats.run()
    elif c == "3": predictor.run()
    elif c == "4": players.run()
    elif c == "5": break
