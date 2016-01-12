import time
start_time = time.time()

import re
print(sum(sum(ord(c)-64 for c in s)*i for i, s in enumerate(sorted(re.findall(r"\"([A-Z]+)\"", open('names.txt', 'r').read())), start=1)))
print("%s seconds" % (time.time() - start_time))