lFile = open('Day_5\\input.txt','r')
lines = lFile.read().splitlines()
count = 0
colors = {}

for line in lines:
    i = line.find('shiny gold')
    if i != -1:
        
