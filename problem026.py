places = 1000

def find_max_pattern(vec):
	cur_max = -1
	cur_offset = -1
	print("Vector: "),
	print(vec)
	for offset1 in xrange(len(vec)):
		for offset2 in xrange(offset1+1, len(vec)):
			ll = 0
			try:
				while vec[offset1+ll] == vec[offset2+ll] and offset2+ll < len(vec)-1 and offset1+ll < offset2:
					ll += 1
			except Exception, e:
				print("O1 = %d, O2 = %d, ll = %d" % (offset1, offset2, ll))
				exit()
			if ll > cur_max:
				cur_max = ll
				cur_offset = offset1
	return cur_max, ''.join(vec[cur_offset:cur_offset+cur_max])

max_div = -1
max_rep_pattern = ''
max_pattern_len = -1

for divisor in xrange(2,1000):
	print("Checking %d..." % divisor),
	val = 10
	nums = []
	for i in xrange(places):
		whole = val / divisor
		val = (val % divisor) * 10
		nums.append(whole)
		if val == 0:
			break
	cur_max, cur_pattern = find_max_pattern(nums)
	if cur_max > max_pattern_len:
		max_pattern_len = cur_max
		max_rep_pattern = cur_pattern
		max_div = divisor
	print("%d [%s]" % (cur_max, cur_pattern))

print("Max divisor %d, length = %d" % (max_div, max_pattern_len))