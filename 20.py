import time
start_time = time.time()

import math
print(sum(list(map(int,list(str(math.factorial(100)))))))

print("%s seconds" % (time.time() - start_time))
