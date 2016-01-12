import time
start_time = time.time()

def factorial(x):
	if x == 0: return 1
	res = 1
	for n in range(1,x + 1):
		res *= n
	return res	  
			
facts	 = [factorial(x) for x in range(0, 101)]
counter	 = 0 
exceeded = True

for n in range(1, 101):
	for r in range(1, n + 1):
		c = facts[n] / (facts[r] * facts[n - r])
		while c > 1000000:
			counter += 1
			r += 1
			c = facts[n] / (facts[r] * facts[n - r])
			if c < 1000000:
				exceeded = False
				break	
		if not exceeded:
			exceeded = True
			break
			
print (counter)
print("%s seconds" % (time.time() - start_time))