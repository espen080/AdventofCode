import numpy

lFile = open('Day_1\\day1Input.txt','r')
lines = lFile.read().splitlines()
arr = numpy.array(lines)
answer = 'The answer is {}. The integers are {} and {}'


for line in arr:
    amt = int(line)
    remain = 2020-amt
    count = numpy.count_nonzero(arr == str(remain))
    if count >= 1:
        x = numpy.where(arr==str(remain))
        amt2 = int(arr[x[0]])
        print(answer.format(str(amt*amt2),str(amt),str(amt2)))
        break