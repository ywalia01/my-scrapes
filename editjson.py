temp = ""
temp2 = ""
counter = 1

with open('allquotes.txt', 'r') as f:
    for line in f:
        line = line.strip()
        temp += line

for x in range(0, len(temp)):
    temp2 += temp[x]
    if temp[x] == '{':
        temp2 += '"id": "' + str(counter) + '",'
        counter += 1

print(temp2)
