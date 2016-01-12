import math
import time

primes = [2]
MaxNum = 2000000

def isPrime(num):
    i=0
    while primes[i]<= int(math.sqrt(num)):
        if num%primes[i] == 0:
            return False
        i += 1
    return True

def main():
    for CurrentNum in range (3, MaxNum, 2):
        if isPrime(CurrentNum):
            primes.append(CurrentNum)

    
    print("Sum of primes: ", MaxNum, " is ", sum(primes), ".",  sep='')
    pass

start_time = time.time()

if __name__ == '__main__':
    main()
    
print("%s seconds" % (time.time() - start_time))