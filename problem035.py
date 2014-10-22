"""

"""

import numpy as np

def generate_primes(n=1000):
	primes = []
	prime_flags = [0]*(n+1)
	for prime in xrange(2, n):
		if prime_flags[prime] == 0:
			primes.append(prime)
		else:
			continue
		mult = 2
		while mult*prime < n:
			prime_flags[mult*prime] = 1
			mult += 1
	return primes

def gen_rotations(val):
	txtval = str(val)
	out = [val]
	for i in xrange(len(txtval)-1):
		txtval += txtval[0]
		txtval = txtval[1:]
		out.append(int(txtval))
	return tuple(set(out))

primes = generate_primes(1000000)
found_circs = []

def is_circular_prime(num):
	global primes
	rots = gen_rotations(num)
	for va in rots:
		if va not in primes:
			return False, None
	return True, rots

for num in primes:
	if num in found_circs:
		continue
	test, rots = is_circular_prime(num)
	if test:
		found_circs += rots

print("Total of %d circular primes" % len(found_circs))
print("Found:")
print(found_circs) # 55