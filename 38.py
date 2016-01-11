from itertools import permutations

numbers = [''.join(p) for p in permutations('123456789')]

numbers.sort()
numbers.reverse()

for n in numbers:
	s1=int(n[:4])
	s2=int(n[4:])
	if s2 / 2 == s1:
		if n in numbers:
			print("%s (%s,%s)" % (n,s1,s2))