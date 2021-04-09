import csv

filename = "dunequotebot.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

    print("Total no. of rows: %d" % (csvreader.line_num))

# print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
# print('\nFirst 5 rows are:\n')
# print(rows[1][11])
print(len(rows[1]))
# for row in rows[:5]:
# for col in row:
# print("%10s" % row(11)),
print('\n')
