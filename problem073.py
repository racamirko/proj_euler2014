"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d =< 8 in ascending order of size, we get:
	1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d =< 12,000?
"""

import numpy as np

combs = set()

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

primes = generate_primes(12000)

def gcd_recursive(a,b): # fails
	if a == b:
		return a
	elif a > b:
		return gcd(a-b, b)
	else:
		return gcd(a, b-a)

def gcd(a,b):
	a1 = a
	b1 = b
	while a1 > 0 and b1 > 0:
		if a1 == b1:
			return a1
		elif a1 > b1:
			a1 = a1 - b1
		else:
			b1 = b1 - a1
	return 1

upper_lim = 1.0/2.0
lower_lim = 1.0/3.0
cnt = 0

def add_to_cnt(a,b):
	global cnt, upper_lim, lower_lim
	val = float(a)/float(b)
	if lower_lim < val < upper_lim:
		cnt += 1

def check_and_add(a,b):
	global combs, primes
	if b in primes or a in primes:
		add_to_cnt(a,b)
	else:
		max_div = gcd(a,b)
		if max_div == 1:
			add_to_cnt(a,b)


for d in xrange(1, 12001): # 12000
	print(d)
	n_beg = int(d*lower_lim) - 1
	n_end = int(d*upper_lim) + 2
	for n in xrange(n_beg, n_end):
		check_and_add(n,d)

print("Found %d" % cnt) # 7295372