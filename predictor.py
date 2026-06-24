def run():
    teams = {
        "1": {"name": "Brazil", "rating": 88, "attack": 90, "defense": 85},
        "2": {"name": "France", "rating": 87, "attack": 89, "defense": 86},
        "3": {"name": "Argentina", "rating": 87, "attack": 91, "defense": 83},
        "4": {"name": "England", "rating": 85, "attack": 86, "defense": 84},
        "5": {"name": "Germany", "rating": 84, "attack": 85, "defense": 84},
        "6": {"name": "Spain", "rating": 85, "attack": 87, "defense": 83},
        "7": {"name": "Portugal", "rating": 84, "attack": 88, "defense": 80},
        "8": {"name": "Netherlands", "rating": 83, "attack": 84, "defense": 82},
    }

    print("\n=== Predict Match ===")
    for k, t in teams.items():
        print(f"{k}. {t['name']}")

    h = input("\nSelect home team number: ")
    a = input("Select away team number: ")

    if h not in teams or a not in teams:
        print("Invalid selection.")
        return

    home = teams[h]
    away = teams[a]

    home_score = (home["attack"] + home["rating"]) / 2
    away_score = (away["attack"] + away["rating"]) / 2

    diff = home_score - away_score
    home_score += 3  # home advantage

    print(f"\n=== Prediction ===")
    print(f"{home['name']} vs {away['name']}")

    if home_score > away_score + 3:
        print(f"Winner: {home['name']} (Strong favourite)")
    elif away_score > home_score:
        print(f"Winner: {away['name']} (Away upset!)")
    else:
        print("Result: Too close to call - could be a draw!")

    print(f"\nStrength: {home['name']} {home_score:.1f} - {away_score:.1f} {away['name']}")
    input("\nPress Enter to go back...")
