import time
start_time = time.time()

def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n
print((fact(40)) / (fact(20) * fact(20)))
print("%s seconds" % (time.time() - start_time))