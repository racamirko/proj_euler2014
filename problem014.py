known_combs = {}

def gen_chain(x):
	if known_combs.has_key(x):
		return known_combs[x]
	if x == 1:
		return 1
	if x % 2 == 0:
		return gen_chain(x / 2) + 1
	else:
		return gen_chain(3*x+1) + 1

max_len = 0
max_num = -1

for x in xrange(1, 1000000):
	chain_len = gen_chain(x)
	# print("%d length = %d" % (x, chain_len))
	known_combs[x] = chain_len
	if chain_len > max_len:
		max_len = chain_len
		max_num = x

print("Max len  %d = %d" % (max_num, max_len))