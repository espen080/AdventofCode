import numpy

lFile = open('C:\\Users\\eklungland001\\AdventofCode\\Day_1\\day1Input.txt','r')
lines = lFile.read().splitlines()
arr = numpy.array(lines)
answer = 'The answer is {}. The integers are {} and {} and {}'
end = False

for i in arr:
    amt = int(i)
    for n in arr:
        amt2 = int(n)
        if amt + amt2 < 2020:
            r = 2020 - amt - amt2
            count = numpy.count_nonzero(arr == str(r))
            if count >= 1:
                x = numpy.where(arr==str(r))
                amt3 = int(arr[x[0]])
                print(answer.format(str(amt*amt2*amt3),str(amt),str(amt2),str(amt3)))
                end = True
                break
    if end:
        break
                
