quotesjson = "[\n"

with open('goodreads_dunequotes.txt', 'r') as f:
    for line in f:
        line = line.strip()
        quotesjson += '\t{"quote": '
        quotesjson += line
        quotesjson += '},\n'

quotesjson += "]"
f.close()

with open('quotes.txt', 'w') as f2:
    f2.write(quotesjson)

print(quotesjson)
