def digitsquaresum(n):
    m = 0
    while n:
        m += (n % 10) ** 2
        n //= 10
    return m


num = 0

for i in range(1, 10**7 + 1):
    while True:
        i = digitsquaresum(i)
        if i == 1:
            break
        if i == 89:
            num += 1
            break
            
print(num)