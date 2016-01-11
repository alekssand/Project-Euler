from functools import reduce

nth = [10**i - 1 for i in range(7)]
frctn = ''.join([str(i) for i in range(1, 2*10**5)])

print(reduce(lambda x, y: x*y, [int(frctn[d]) for d in nth]))