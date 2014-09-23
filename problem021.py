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
	rez.sort()
	return rez

# print(np.array(get_divisors(220)).sum())
# print(np.array(get_divisors(284)).sum())
# exit()

total_sum = 0
found_pairs = []
for n in xrange(1, 10000):
	if n in found_pairs:
		continue
	divs1_sum = np.array(get_divisors(n)).sum()
	divs2_sum = np.array(get_divisors(divs1_sum)).sum()
	if divs2_sum == n and divs1_sum != n:
		total_sum += n
		total_sum += divs1_sum
		found_pairs.append(n)
		found_pairs.append(divs1_sum)

print(total_sum)
