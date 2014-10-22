"""
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

Authors note:
There should be a nicer way to do this... I was just tired.
"""

import numpy as np

in_fname = "p089_roman.txt"
in_hnd = open(in_fname)

def decode_number(rnum):
	rezsum = 0
	skip_nums = 0
	for i in xrange(len(rnum)):
		if skip_nums > 0:
			skip_nums -= 1
			continue
		if rnum[i] == 'M':
			rezsum += 1000
			continue
		if rnum[i] == 'D':
			if i+1 < len(rnum) and rnum[i+1] == 'M':
				rezsum += 500
				skip_nums = 1
				continue
			else:
				rezsum += 500
				continue
		if rnum[i] == 'C':
			if i+1 < len(rnum) and rnum[i+1] == 'M':
				rezsum += 900
				skip_nums = 1
				continue
			elif i+1 < len(rnum) and rnum[i+1] == 'D':
				rezsum += 400
				skip_nums = 1
				continue
			else:
				rezsum += 100
				continue
		if rnum[i] == 'L':
			if i+1 < len(rnum) and rnum[i+1] == 'C':
				rezsum += 50
				skip_nums = 1
				continue
			else:
				rezsum += 50
				continue
		if rnum[i] == 'X':
			if i+1 < len(rnum) and rnum[i+1] == 'C':
				rezsum += 90
				skip_nums = 1
				continue
			else:
				rezsum += 10
				continue
		if rnum[i] == 'V':
			if i+1 < len(rnum) and rnum[i+1] == 'X':
				rezsum += 5
				skip_nums = 1
				continue
			else:
				rezsum += 5
				continue
		if rnum[i] == 'I':
			if i+1 < len(rnum) and rnum[i+1] == 'X':
				rezsum += 9
				skip_nums = 1
				continue
			else:
				rezsum += 1
				continue
	return rezsum

def encode_number(val):
	out_txt = []
	rest = val
	for i in xrange(rest / 1000):
		out_txt.append('M')
	rest %= 1000
	if rest >= 900:
		out_txt.append('CM')
		rest -= 900
	if rest >= 500:
		out_txt.append('D')
		rest -= 500
	if rest >= 400:
		out_txt.append('CD')
		rest -= 400
	for i in xrange(rest / 100):
		out_txt.append('C')
	rest %= 100
	if rest >= 90:
		out_txt.append('XC')
		rest -= 90
	if rest >= 50:
		out_txt.append('L')
		rest -= 50
	if rest >= 40:
		out_txt.append('XL')
		rest -= 40
	for i in xrange(rest / 10):
		out_txt.append('X')
	rest %= 10
	if rest >= 9:
		out_txt.append('IX')
		rest -= 9
	if rest >= 5:
		out_txt.append('V')
		rest -= 5
	if rest >= 4:
		out_txt.append('IV')
		rest -= 4
	for i in xrange(rest):
		out_txt.append('I')
	return ''.join(out_txt)

all_lines = in_hnd.readlines()
total_saved = 0
for in_txt in all_lines:
	in_txt = in_txt.strip()
	val = decode_number(in_txt)
	out_txt = encode_number(val)
	saved_chars = max(len(in_txt)-len(out_txt), 0)
	total_saved += saved_chars
	print("%s : %d : %s, saved: %d" % ( in_txt, val, out_txt, saved_chars))
print('Total saved: %d' % total_saved) # 743
