import time
start_time = time.time()

import math
print (sum(i for i in range(3, 10**6) if i == sum(math.factorial(int(c)) for c in str(i))))
print("%s seconds" % (time.time() - start_time))