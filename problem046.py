"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import numpy as np

def generate_primes(n=1000):
	primes = [1]
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

primes = generate_primes(10000)

for i in xrange(1,10000, 2):
	print("%d: " % i),
	found = False
	for prime in primes:
		print("%d," % prime),
		if prime > i:
			break
		rez = ((i-prime)/2)**0.5
		if rez == int(rez):
			print("found %d+2*%d^2" % (prime, rez))
			found = True
			break
	if not found:
		print("\n%d couldn't be formulated as parts" % i)
		break
