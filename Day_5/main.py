lFile = open('Day_5\\input.txt','r')
lines = lFile.read().splitlines()

def getReduction(rng, chars, hl):
    i = 0
    while i < len(chars):
        l = int(rng[0])
        h = int(rng[1])
        s = int((h+1-l)/2)
        c = chars[i]
        if c == hl[0]:
            rng[1] = h - s
        elif c == hl[1]:
            rng[0] = l + s
        i+=1
    if rng[0] == rng[1]:
        return rng[0]
    else:
        return None

maxId = 0

for line in lines:
    row = getReduction([0,127],line[0:7],['F','B'])
    col = getReduction([0,7],line[7:10],['L','R'])
    id = row * 8 + col

    if id > maxId:
        maxId = id
print(maxId)

'Part 2'
ids = []
for line in lines:
    row = getReduction([0,127],line[0:7],['F','B'])
    col = getReduction([0,7],line[7:10],['L','R'])

    id = row * 8 + col
    ids.append(id)

i = 0
while i <= len(ids):
    if i not in ids and i-1 in ids and i+1 in ids:
        print(i)
    i+=1

