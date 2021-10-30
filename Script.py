import csv
import os

map = {}

with open('methods.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        map[row[0]] = row[1]

with open('params.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        map[row[0]] = row[1]

with open('fields.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        map[row[0]] = row[1]

print("Remapping...")
for subdir, dirs, files in os.walk('./'):
    for file in files:
        if file.endswith(".java"):
            f = open(file, "rt")
            data = f.read()
            for a,b in map.items():
                data = data.replace(a, b)
            f.close()
            f = open(file, "wt")
            f.write(data)
            f.close
            
print("Finished!")