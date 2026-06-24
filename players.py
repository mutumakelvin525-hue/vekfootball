def run():
    players = {
        "1": {"name": "Messi", "country": "Argentina", "goals": 98, "assists": 56, "wc_goals": 13, "speed": 85, "dribbling": 96},
        "2": {"name": "Ronaldo", "country": "Portugal", "goals": 128, "assists": 41, "wc_goals": 8, "speed": 87, "dribbling": 89},
        "3": {"name": "Mbappe", "country": "France", "goals": 48, "assists": 38, "wc_goals": 12, "speed": 97, "dribbling": 92},
        "4": {"name": "Neymar", "country": "Brazil", "goals": 79, "assists": 56, "wc_goals": 8, "speed": 90, "dribbling": 94},
        "5": {"name": "Haaland", "country": "Norway", "goals": 75, "assists": 30, "wc_goals": 0, "speed": 89, "dribbling": 80},
        "6": {"name": "Benzema", "country": "France", "goals": 77, "assists": 58, "wc_goals": 8, "speed": 78, "dribbling": 87},
        "7": {"name": "Salah", "country": "Egypt", "goals": 71, "assists": 45, "wc_goals": 2, "speed": 91, "dribbling": 90},
        "8": {"name": "Lewandowski", "country": "Poland", "goals": 82, "assists": 57, "wc_goals": 10, "speed": 78, "dribbling": 82},
    }

    print("\n=== Compare Players ===")
    for k, p in players.items():
        print(f"{k}. {p['name']} ({p['country']})")

    a = input("\nSelect first player: ")
    b = input("Select second player: ")

    if a not in players or b not in players:
        print("Invalid selection.")
        return

    p1 = players[a]
    p2 = players[b]

    print(f"\n{'Stat':<15} {p1['name']:<15} {p2['name']}")
    print("-" * 40)
    for stat in ["goals", "assists", "wc_goals", "speed", "dribbling"]:
        v1 = p1[stat]
        v2 = p2[stat]
        winner = "<--" if v1 > v2 else ("-->" if v2 > v1 else "===")
        print(f"{stat:<15} {str(v1):<15} {v2} {winner}")

    input("\nPress Enter to go back...")
