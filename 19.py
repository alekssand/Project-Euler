import time
start_time = time.time()

def getDayOfWeek(n):
	days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	return days[n%7]

ans = 0
count =1
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
for d in range(1901,2001):
	for f in months:
		if f=="January" or f=="March" or f=="May" or f=="July" or f=="August" or f=="October" or f=="December":
			if getDayOfWeek(count)=="Sunday":
				count=count+31
				ans = ans+1
			else:
				count = count+31
		elif f=="February":
			if d%4==0:
				if getDayOfWeek(count)=="Sunday":
					count=count+29
					ans=ans+1
				else:
					count=count+29
			else:
				if getDayOfWeek(count)=="Sunday":
					count=count+28
					ans=ans+1
				else:
					count=count+28
		else:
			if getDayOfWeek(count)=="Sunday":
				count=count+30
				ans = ans+1
			else:
				count = count+30
print (ans)
print("%s seconds" % (time.time() - start_time))
