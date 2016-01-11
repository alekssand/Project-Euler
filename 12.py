import time
import math

def triangle_num(idx):
    sum = 0
    for i in range(idx + 1):
        sum += i
    return sum

def find_divisor(num):
    count = 2
    i = 2
    while(num > i*i):
        if num % i == 0:
            count += 2
        i += 1
        
    if i*i == num:
        count += 1
    
    return count
            
            
            
def find(div_count):
    start = time.time()
    
    i = 0
    while find_divisor(triangle_num(i)) < div_count:
        i += 1
        find_divisor(triangle_num(i))
        
    print (time.time() - start)
    print (triangle_num(i))
        
find(500)