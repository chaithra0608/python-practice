players = [
    {"name": "Patrick Mahomes", "position": "QB", "jersey": 15, "yards": 4100, "touchdowns": 34},
    {"name": "Travis Kelce", "position": "TE", "jersey": 87, "yards": 1200, "touchdowns": 9},
    {"name": "Isiah Pacheco", "position": "RB", "jersey": 10, "yards": 935, "touchdowns": 7},
    {"name": "Chris Jones", "position": "DT", "jersey": 95, "yards": 0, "touchdowns": 0},  # Defensive player
]

positions = [player["position"] for player in players]
print("Player Positions:", positions)

print("\nBefore update:", players[2])  
players[2]["yards"] += 100 
players[2]["touchdowns"] += 1  
print("After update:", players[2])

total_yards = sum(player["yards"] for player in players)
total_touchdowns = sum(player["touchdowns"] for player in players)
num_players = len(players)

avg_yards = total_yards / num_players
avg_touchdowns = total_touchdowns / num_players

print("\nAverage Yards:", round(avg_yards, 2))
print("Average Touchdowns:", round(avg_touchdowns, 2))

