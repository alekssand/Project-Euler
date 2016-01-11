import math

def is_prime(n, known_primes):
    sqrt_n = math.sqrt(n)
    for prime in known_primes:
        if prime > sqrt_n:
            break
        if n % prime == 0:
            return False

    return True

primes = [2]
count = 1
num = 1

while count < 10001:
    num += 2

    if is_prime(num, primes):
        count += 1
        primes.append(num)

print('10,001st prime: ' + str(num))