import sys

i = [int(x) for x in open('input')]
sums = set()
sum = 0
while True:
    for x in i:
        sum += x
        if sum in sums:
            print sum
            sys.exit(1)    

        sums.add(sum)
