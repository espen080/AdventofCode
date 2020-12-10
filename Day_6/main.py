lFile = open('Day_6\\input.txt','r')
groups = lFile.read().split('\n\n')
count = 0

for group in groups:
    count+= len(set(group.replace('\n','').strip()))
print (count)

'Part 2'

def intersect(lists):
    return list(set.intersection(*map(set, lists)))

count=0
for group in groups:
    count += len(intersect(group.split('\n')))

print(count)