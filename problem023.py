import numpy as np

def get_divisors(x):
	rez = [1]
	top_bar = x/2+1
	for i in xrange(2, x/2+1):
		if i >= top_bar:
			break
		div_whole = x / i
		if x % i == 0:
			rez.append(i)
			rez.append(div_whole)
			if div_whole < top_bar:
				top_bar = div_whole
	return sorted(set(rez)) # cheap trick :(

def number_type(x):
	sum_factors = np.array(get_divisors(x)).sum()
	if sum_factors < x:
		return -1
	elif sum_factors == x:
		return 0
	else:
		return 1

def gen_abund_nums():
	abund_nums = []
	for i in xrange(1, 28124):
		if number_type(i) == 1:
			# print("%d, " % i),
			abund_nums.append(i)
	abund_nums.sort()
	return abund_nums

abund_nums = np.array(gen_abund_nums())
print("")

print("Found %d aboundant numbers" % len(abund_nums) )
total_sum = 0
for n in xrange(1, 28124):
	mat = np.ones(len(abund_nums)) * n
	diff = mat - abund_nums
	if len(np.intersect1d(diff, abund_nums)) == 0:
		print('.'),
		total_sum += n
print("")
print(total_sum)