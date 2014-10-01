found_combs = set()

def form_key(a,b,c):
	ll = [a,b,c]
	ll.sort()
	return tuple(ll)


def check_pandigital(a,b,c):
	all_nums = str(a)+str(b)+str(c)
	if len(all_nums) < 9:
		return False
	if '0' in all_nums:
		return False
	sum_num = reduce(lambda x, y: int(x)+int(y), all_nums)
	if sum_num != 1+2+3+4+5+6+7+8+9:
		return False
	for x in xrange(1,10):
		if str(x) not in all_nums:
			return False
	return True

# print(check_pandigital(123, 456, 789))
# print(check_pandigital(182, 456, 888))

for x in xrange(1,1000):
	x_s = str(x)
	if '0' in x_s:
		continue
	pwr = (9-len(x_s))/2-1
	for y in xrange(10**pwr, 10**(pwr+1)):
		if '0' in str(y):
			continue
		z = x*y
		if check_pandigital(x,y,z):
			found_combs.add(form_key(x,y,z))

total_sum = 0
found_products = []
for cc in found_combs:
	print("Comb: %d, %d, %d" % cc)
	prod = max(cc)
	if prod not in found_products:
		total_sum += prod
		found_products.append(prod)

print("Total sum: %d" % total_sum)