all_letts = "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split(' ') #because I'm never sure about the order
all_letts.sort()

in_filename = "DOWNLOAD FILE AND ADD PATH"
in_fh = open(in_filename)
line = in_fh.readline()

names = []
for name in line.split(","):
	names.append(name[1:-1])
names.sort()

def score(n):
	sub = 0
	for letter in n:
		sub += all_letts.index(letter)+1
	return sub

total_sum = 0
for i in xrange(len(names)):
	total_sum += (i+1)*score(names[i])

print(total_sum) # 871198282