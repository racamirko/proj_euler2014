
import itertools
perms = itertools.permutations('0123456789', 10)
no = 0
for i in perms:
	no += 1
	# print("%d = %s" % (no, ''.join(i)))
	if no == 1000000:
		print(''.join(i))
		break