import time
start_time = time.time()

a=1
b=1
indexFib = 3

while(len(str(a+b)) < 1000):
	a=a+b
	b=a-b
	indexFib += 1
	
print(indexFib)
print("%s seconds" % (time.time() - start_time))