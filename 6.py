import time
start_time = time.time()

def g(n): 
    sum1,sum2=0,0 
    for i in range(1,n+1): 
        sum1 += i**2 
        sum2 += i 
    return abs(sum1 - sum2**2) 

print (g(100))
print("%s seconds" % (time.time() - start_time))