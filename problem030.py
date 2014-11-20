"""

"""

import sys
import matplotlib.pyplot as plt
import numpy as np

def pow_of_nums(x):
	tmp_sum = 0
	while x > 0:
		num = x % 10
		x /= 10
		tmp_sum += num**5
	return tmp_sum

print(pow_of_nums(999))

# sys.exit()

vals = []
total_sum = 0
for x in xrange(2,400000):
	other_num = pow_of_nums(x)
	vals.append(other_num)
	if other_num == x:
		total_sum += x

print(total_sum)

plt.plot(np.arange(2,400000), vals)
plt.show()