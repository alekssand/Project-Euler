import time
start_time = time.time()


import math
items="0123456789"

count=0
wantedNumber=1000000

def allOptions(l,n):
	l+=str(n)
	global items,count
	leftItems=[]
	if math.factorial(len(items)-len(l))+count<wantedNumber:
		count+=math.factorial(len(items)-len(l))
		return

	for item in items:
		if str(item) not in l and count<wantedNumber:
			allOptions(l,item)

	if(len(l)==len(items)):
		count+=1
		if count==wantedNumber:
			print(l)

for item in items:
	allOptions("",item)
        
print("%s seconds" % (time.time() - start_time))