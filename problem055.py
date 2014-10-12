"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
	349 + 943 = 1292,
	1292 + 2921 = 4213
	4213 + 3124 = 7337
That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
"""

import numpy as np

def check_palin(x):
	txt = str(x)
	for i in xrange(len(txt)/2):
		if txt[i] != txt[-(i+1)]:
			return False
	return True

def make_mirror(x):
	tmp = list(str(x))
	tmp.reverse()
	return int(''.join(tmp))

def check_has_palin(x, max_depth=50):
	cur_val = x
	for i in xrange(max_depth):
		x1 = make_mirror(cur_val)
		new_val = cur_val + x1
		if check_palin(new_val):
			return True
		cur_val = new_val
	return False

# print(check_palin(121))
# print(check_palin(467764))
# print(check_palin(467714))
# print(check_palin(467364))

# print(make_mirror(12345))

palin_cnt = 0
for x in xrange(1, 10000):
	print("Testing: %d" % x)
	if not check_has_palin(x):
		palin_cnt += 1

print("Found %d lychrel numbers" % palin_cnt) # 249