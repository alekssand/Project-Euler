import time
start_time = time.time()
print(sum([i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0)]))
print("%s seconds" % (time.time() - start_time))
