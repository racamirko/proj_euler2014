places = 5000

def find_max_pattern(vec):
	cur_max = 0
	cur_offset = 0
	# print("Vector: "),
	# print(vec)
	for offset in xrange(len(vec)):
		for cycle_len in xrange(1, len(vec)-offset):
			found_valid = True
			init_vector = vec[offset:offset+cycle_len]
			# print("Initial vector: "),
			# print(init_vector)
			if len(vec) - offset <= 2*cycle_len:
				continue # too long for check
			for offset2 in xrange(offset+cycle_len, len(vec)-cycle_len, cycle_len):
				# print("."),
				sub_vec2 = vec[offset2:offset2+cycle_len]
				if init_vector != sub_vec2:
					found_valid = False
					break
			# print("")
			if found_valid:
				return cycle_len, ''.join(map(lambda x: str(x), init_vector))
	return cur_max, ''

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