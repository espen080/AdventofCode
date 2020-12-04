lFile = open('Day_3\\input.txt','r')
lines = lFile.read().splitlines()

counter = 0
right = 0
down = 0

for line in lines:
    right+= 3
    down+=1
    if down < len(lines):
        nLine = lines[down]
        while len(nLine) < right:
            nLine += nLine
        if nLine[right]=='.':
            pass
        elif nLine[right]=='#':
            counter+=1
print(counter)

'Part 2'

