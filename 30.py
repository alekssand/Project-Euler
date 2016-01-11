sumnums=0
for a in range(4150,194980):
	cursum=0
	for d in str(a):
		cursum= cursum + int(d)**5
	if cursum==a:
		sumnums = sumnums+a
print (sumnums)