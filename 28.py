import time
start_time = time.time()

print (sum((((dim**2)*4) - (dim-1)*6) for dim in range (3, 1002, 2))+1)
print("%s seconds" % (time.time() - start_time))