quotesjson = "["
temp = ""
counter = 1
with open('allquotes.txt', 'r') as f:
    for line in f:
        line = line.strip()
        quotesjson += '{"id": "'
        quotesjson += str(counter)
        quotesjson += '",'
        quotesjson += '"quote": '
        quotesjson += line
        quotesjson += '},'
        counter += 1

quotesjson += "]"
f.close()

with open('quotes.txt', 'w') as f2:
    f2.write(quotesjson)

print(quotesjson)
