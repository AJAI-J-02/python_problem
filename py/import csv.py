import csv

data = [
    ["Player", "Team", "Role", "ODI Average"],
    ["Saurav Ganguly", "India", "Hard Hitter", 41],
    ["Kane Williamson", "New Zealand", "Aspirant", 49.2],
    ["Ricky Ponting", "Australia", "Accumulator", 42],
    ["Kevin Peterson", "England", "Hard Hitter", 40.7],
    ["Lance Klusener", "South Africa", "Accumulator", 41.1]
]

with open("player.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)
print("Data has been written to players.csv")