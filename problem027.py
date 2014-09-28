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

primes = generate_primes()

print("Length : %d" % len(primes))

# generate combinations
max_a = -1
max_b = -1
max_length = 0
for a in xrange(-1000, 1000):
	for b in xrange(-1000, 1000):
		ll = -1
		for n in xrange(1000):
			if not n**2+a*abs(n)+b in primes:
				ll = n
				break
		if ll > max_length:
			max_a = a
			max_b = b
			max_length = ll
			print("tt: a=%d, b=%d, length=%d, product=%d" % (max_a, max_b, max_length, max_a*max_b))

print("a=%d, b=%d, length=%d, product=%d" % (max_a, max_b, max_length, max_a*max_b))
