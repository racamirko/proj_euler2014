"""
	Bouncy numbers
"""

def increasing_num(x):
	txt = str(x)
	for i in xrange(1,len(txt)):
		if int(txt[i-1]) > int(txt[i]):
			return False
	return True

def decreasing_num(x):
	txt = str(x)
	for i in xrange(1,len(txt)):
		if int(txt[i-1]) < int(txt[i]):
			return False
	return True

def bouncy_num(x):
	if not increasing_num(x) and not decreasing_num(x):
		return True
	return False

# print(increasing_num(134468))
# print(decreasing_num(66420))
# print(bouncy_num(155349))

bouncies = 0.0
for n in xrange(5000000):
	if bouncy_num(n):
		bouncies += 1.0
		pcts = bouncies/float(n)*100.0
		if pcts >= 99.0:
			print("At %d found %d bouncies (%.2f%%)" % (n, bouncies, pcts))
			break