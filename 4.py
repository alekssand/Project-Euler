import time

first = 0
second = 0; 
greatest = 0
 

start = time.clock()


for x in range (100, 999):
    for y in range (100, 999):
        first = str(x*y)
        if first == first[::-1]:
            if greatest < (x*y):
                greatest = (x*y)
                print(greatest)
    

end = (time.clock() - start)

test = str(123123)
print(test[::-1])

print(greatest)
print(end)