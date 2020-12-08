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

def getTrees(r, d):
    counter = 0
    right = 0
    down = 0

    for line in lines:
        right += r
        down+=d
        if down < len(lines):
            nLine = lines[down]
            while len(nLine) <= right:
                nLine += nLine
            if nLine[right]=='.':
                pass
            elif nLine[right]=='#':
                counter+=1
    return counter

print(getTrees(1,1)*getTrees(3,1)*getTrees(5,1)*getTrees(7,1)*getTrees(1,2))