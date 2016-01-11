
import time
start_time = time.time()

number = 600851475143
primeFactors = []
runningFactor = 2

while number != 1:
    if number % runningFactor == 0:
        if runningFactor not in primeFactors:
            primeFactors.append(runningFactor)
            
        number/= runningFactor
        runningFactor = 2
    else:
        runningFactor+= 1
        
print(primeFactors)

print("--- %s seconds ---" % (time.time() - start_time))