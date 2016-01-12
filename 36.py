import time
start_time = time.time()

print (sum(x for x in range(10**6) if str(x) == str(x)[::-1] and bin(x)[2:] == bin(x)[2:][::-1]))
print("%s seconds" % (time.time() - start_time))