import time
start_time = time.time()

first = 0
second = 0; 
greatest = 0
 
for x in range (100, 999):
    for y in range (100, 999):
        first = str(x*y)
        if first == first[::-1]:
            if greatest < (x*y):
                greatest = (x*y)
                print(greatest)
    
test = str(123123)
print(greatest)
print("%s seconds" % (time.time() - start_time))
