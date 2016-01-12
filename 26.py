import time
start_time = time.time()

def pow(a, b):
    result = 1
    for i in range(b + 1):
        result = result * a
    return result


def multiplicative_order(a, n):
    k = 1
    while True:
        v = pow(a, k)
        m = v % n
        if m == 1:
            return k
        k += 1


def repetend_length(p):
    return multiplicative_order(10, p)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def coprime(a, b):
    return gcd(a, b) == 1


max_p = 2
max_repetend_length = 0
for p in range(2, 1000):
    if coprime(10, p):
        rep_length = repetend_length(p)
        if rep_length > max_repetend_length:
            max_repetend_length = rep_length
            max_p = p

print(max_p)
print("%s seconds" % (time.time() - start_time))