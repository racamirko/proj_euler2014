x = 2**1000
ss = 0
while x > 0:
	ss += x % 10
	x /= 10
print(ss)

exit(0)