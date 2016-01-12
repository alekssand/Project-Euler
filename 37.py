import time
start_time = time.time()

def is_truncatable(n):
    for d in range(1, len(str(n))):
        if not is_prime(str(n)[d:]) or not is_prime(str(n)[:d]): 
            return False 
    return True

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def generate_attempts(attemptsArray,n):
    for attempt in attemptsArray[:]:
        for number in numbers:
            if (not attempt.endswith(number)) and is_prime(int(attempt)):
                if is_prime(int(str(attempt) + str(number))):
                    attemptsArray.append(str(attempt) + str(number))
        attemptsArray.remove(attempt)
        
    n-=1
    if n > 1:
        return generate_attempts(attemptsArray,n)
    else:
        return attemptsArray           
        
tp = []
numbers=['1','2','3','5','7','9']
numLen = 2
while len(tp)<11:
    attemptsArray = generate_attempts(numbers[:],numLen)
    for attempt in attemptsArray:
        if is_truncatable(attempt):
            tp.append(int(attempt))
    numLen+=1
    
print(sum(tp))
print("%s seconds" % (time.time() - start_time))