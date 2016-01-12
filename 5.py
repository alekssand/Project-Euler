import time
start_time = time.time()
number = 20
def isDivisible(num):
    for x in range(2,21):
        if num % x != 0:
            return False
    return True

while not isDivisible(number):
    number+= 10
    
print('The number: ' + str(number))
print("%s seconds" % (time.time() - start_time))
