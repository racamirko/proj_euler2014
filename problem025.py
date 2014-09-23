import numpy as np

prev = 1.0
cur = 1.0
cur_num_digs = 1
index = 2

while cur_num_digs < 1000:
	next_n = cur + prev
	prev = cur
	cur = next_n
	if cur > 10.0:
		cur /= 10.0
		prev /= 10.0
		cur_num_digs += 1
	index += 1

print(index)