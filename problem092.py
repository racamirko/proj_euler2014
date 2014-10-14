"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,
44 > 32 > 13 > 10 > 1 > 1
85 > 89 > 145 > 42 > 20 > 4 > 16 > 37 > 58 > 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
"""

import numpy as np

def create_next(x):
	tmp_sum = 0
	while x > 0:
		tmp_sum += (x % 10)**2
		x /= 10
	return tmp_sum
	

def create_chain(x):
	chain = []
	next_num = x
	while 1:
		if next_num == 89:
			return True
		elif next_num == 1:
			return False
		elif next_num in chain:
			return False
		chain.append(next_num)
		next_num = create_next(next_num)

total_found = 0
for x in xrange(1,10000000):
	if x % 10000 == 0:
		print(x)
	if create_chain(x):
		total_found += 1

print("Found %d" % total_found) # 8581146
