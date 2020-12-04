import re

lFile = open('Day_2\\day2Input.txt','r')
lines = lFile.read().splitlines()
counter = 0

for line in lines:
    num = re.findall('\d+',line)
    min = int(num[0])
    max = int(num[1])
    chars = re.findall('[a-z]+',line)
    char = chars[0]
    pw = chars[1]
    count = str(pw).count(char)
    if count >= min and count <= max:
        counter += 1
    
print(counter)

'Part 2'
counter = 0

for line in lines:
    num = re.findall('\d+',line)
    min = int(num[0])-1
    max = int(num[1])-1
    chars = re.findall('[a-z]+',line)
    char = chars[0]
    pw = chars[1]
    if pw[min] == char and pw[max] == char:
        pass
    elif pw[min] == char or pw[max] == char:
        counter += 1
    
print(counter)