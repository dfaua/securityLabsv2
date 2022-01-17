import csv

file = open('from_weak_csv.txt', 'w')
with open('weak.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = row[0]
        file.write(temp + '\n')

