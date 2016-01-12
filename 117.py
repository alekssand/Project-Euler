import time
start_time = time.time()

max=50

rgb=[0,1,2,4,8]
for i in range(5,max+1):
  rgb.append(rgb[-1]+rgb[-2]+rgb[-3]+rgb[-4])

print(rgb[-1])
print("%s seconds" % (time.time() - start_time))

