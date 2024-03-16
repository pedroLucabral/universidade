import csv

table = {}

with open("leagueChampions.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader.fieldnames:
        table[i] = []
    
    for column in reader:
        for i in column:
            table[i].append(column[i])

print(table)