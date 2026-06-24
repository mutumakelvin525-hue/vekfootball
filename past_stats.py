def run():
    finals = {
        "2022": {"home": "Argentina", "away": "France", "score": "3-3 (AET, ARG won on penalties)", "venue": "Qatar"},
        "2018": {"home": "France", "away": "Croatia", "score": "4-2", "venue": "Russia"},
        "2014": {"home": "Germany", "away": "Argentina", "score": "1-0", "venue": "Brazil"},
        "2010": {"home": "Spain", "away": "Netherlands", "score": "1-0", "venue": "South Africa"},
        "2006": {"home": "Italy", "away": "France", "score": "1-1 (ITA won on penalties)", "venue": "Germany"},
    }

    print("\n=== Past World Cup Finals ===")
    for year, f in finals.items():
        print(f"\n{year} ({f['venue']}):")
        print(f"  {f['home']} vs {f['away']}")
        print(f"  Score: {f['score']}")
    
    input("\nPress Enter to go back...")
