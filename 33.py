import time
start_time = time.time()

for den in range(11, 100):
    if den % 10 == 0:
        continue
    
    for num in range(10, den):
        spam = [[num/10, num%10], [den/10, den%10]]
        egg = [0, 0]
        
        if spam[0][0] == spam[1][0]:
            egg = [num%10, den%10]
        elif spam[0][0] == spam[1][1]:
            egg = [num%10, den/10]
        elif spam[0][1] == spam[1][0]:
            egg = [num/10, den%10]
        elif spam[0][1] == spam[1][1]:
            egg = [num/10, den/10]
        
        if egg[0] and egg[1]:
            if num*egg[1] == den*egg[0]:
                print (num, den+1)
                print("%s seconds" % (time.time() - start_time))