import time
start_time = time.time()

def prime(k):
    for t in range(2,int(k**0.5)+1):
            if k%t==0:
                return False
    return True
def pan(j):
    r=list(str(j))
    y=max(r)
    if len(r)!=int(y):
        return False
    for w in range(1,int(y)):
        if (not(str(w) in r)) or '0' in r :
            return False
    return True
for a in range(17,7654321,2):
    if prime(a) and pan(a):
        print (a)
        print("%s seconds" % (time.time() - start_time))