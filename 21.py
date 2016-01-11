from datetime import datetime

def divisor_sum(x):
	
	d_s = []
	d = 0
	for k in range(1,x):
		d = x%k
		if d == 0:
			d_s.append(k)
		else:
			continue
	return sum(d_s)
	
def main():
	a = 0
	a_d_s = 0
	b = 0
	b_d_s = 0
	ans = []
	for k in range(1,10000):
		a = k
		a_d_s = divisor_sum(a)
		b = a_d_s
		b_d_s = divisor_sum(b)
		if a == b:
			continue
		elif b_d_s == a and a not in ans and b not in ans:
			ans.append(a)
			ans.append(b)
		else:
			continue
	return sum(ans)

start = datetime.now()
k = main()
stop = datetime.now()
delta = stop - start
print(k)
print(delta)