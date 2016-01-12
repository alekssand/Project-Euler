import math, time

def allPermutColour(countTuple):
    countBlack, countColour = countTuple
    sum_ = countBlack + countColour 
    return math.factorial(sum_)/(math.factorial(countBlack) * math.factorial(countColour))


def partitions(n):  
	if n == 0: 
		yield [] 
		return
	for p in partitions(n-1):
		yield [1] + p
		if p and (len(p) < 2 or p[1] > p[0]):
			yield [p[0] + 1] + p[1:]
			
start_time = time.time()

total = 50
sizeRed, sizeGreen, sizeBlue = 2, 3, 4
PermutRed, PermutGreen, PermutBlue = 0, 0, 0
permutRedDict, permutGreenDict, permutBlueDict = {}, {}, {}
for comb in partitions(total):
    setComb = set(comb)
    count1 = comb.count(1)
    if 2 in setComb:
        countRed = comb.count(sizeRed)
        countRedTuple = (count1, countRed)
        if count1 + countRed == len(comb): 
            permutRed = allPermutColour(countRedTuple)
            permutRedDict[countRedTuple] = permutRed
    elif 3 in setComb:
        countGreen = comb.count(sizeGreen)
        countGreenTuple = (count1, countGreen)
        if count1 + countGreen == len(comb): 
            permutGreen = allPermutColour(countGreenTuple)
            permutGreenDict[countGreenTuple] = permutGreen
    elif 4 in setComb:
        countBlue = comb.count(sizeBlue)
        countBlueTuple = (count1, countBlue)
        if (count1 + countBlue == len(comb)):
            permutBlue = allPermutColour(countBlueTuple)
            permutBlueDict[countBlueTuple] = permutBlue

res1 = sum(permutRedDict.values())
res2 = sum(permutGreenDict.values())
res3 = sum(permutBlueDict.values())
print "Ordered Partitions with Red Tiles(size =2):   ", res1
print "Ordered Partitions with Green Tiles(size=3):    ", res2
print "Ordered Partitions with Blue Tiles(size=4):       ", res3
print "                                          ----------------"
print "Total of different ordered partitions:        ", res1 + res2 + res3
print
print"%s seconds" % (time.time() - start_time)