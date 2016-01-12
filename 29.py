import time
start_time = time.time()

upper_bound = 100 

powers = set()

for i in range(2, upper_bound + 1):
    for j in range(2, upper_bound + 1):
        powers.add(i**j)
        powers.add(j**i)

print(len(powers))
print("%s seconds" % (time.time() - start_time))