import re

lFile = open('Day_4\\input.txt','r')
ps = lFile.read().split('\n\n')

reqTags = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
counter=0

for p in ps:
    missing = False
    for tag in reqTags:
        if p.find(tag) == -1:
            missing = True
        
    if not missing:
        counter+=1
print(counter)

'Part 2'
reqTags = {'byr':'(19[2-9][0-9])|(200[0-2])',
        'iyr':'(201[0-9])|(2020)',
        'eyr':'(202[0-9])|(2030)',
        'hgt':'((1[5-8][0-9]cm)|(19[0-3]cm))|((59in)|(6[0-9]in)|(7[0-6]in))',
        'hcl':'(#[0-9a-f]{6})',
        'ecl':'amb|blu|brn|gry|grn|hzl|oth',
        'pid':'\d{9}'}
counter=0
for p in ps:
    fields = p.replace('\n',' ').split(' ')
    psprt = {}
    for field in fields:
        fs = field.split(':')
        psprt.update({fs[0]:fs[1]})
    missing = False
    for key in reqTags.keys():
        rx = reqTags.get(key)
        value = psprt.get(key)
        if value == None:
            missing = True
        elif re.search(rx,value) == None:
            missing = True

    if not missing:
        counter+=1
print(counter)