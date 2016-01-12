from functools import reduce

def calcE(m):
	n, d = m + 1, 1
	for i in range(m, 2, -2): n, d, m = n + d + (m - 2) * (d + n + n), d + n + n, m - 2
	return reduce(lambda x, y: int(x) + int(y), str(n * 3 + d * 2))
    
print(calcE(66))