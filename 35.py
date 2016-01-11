def isPrime(n):
    if n<2: return False
    if n==2: return True
    if not n&1: return False
    for x in range(3,int(n**0.5)+1,2):
        if n%x==0: return False
    return True 

def rotate(n):
    s = str(n)
    r = []
    for i in s:
        s = s[1:]+s[0]
        if s[0]!='0':
            r.append(int(s))
    return r

c = 0        
lim = int(input('upper limit: '))
for n in range(10,lim+1):
    if isPrime(n):
        r = rotate(n)
        for x in r:
            if not isPrime(x): break
        else:
            c += 1

print('Number of circular primes <upper limit: ',c+4)