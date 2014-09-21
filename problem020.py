import math

val = math.factorial(100)
ss = 0
while val > 0:
	ss += val % 10
	val /= 10
print(ss)