sols = set()

for i in range(1000,10000):
    for j in range(2,100):
        if i % j == 0:
            k = i // j
            s = str(i) + str(j) + str(k)
            if len(s) == 9 and ''.join(sorted(s)) == '123456789':
                sols.add(i)
                print("{} * {} == {}".format(j,k,i))

print("the solution is",sum(sols))