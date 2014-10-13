"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

import numpy as np
import pandas as pd

in_filename = '/home/raca/Downloads/p081_matrix.txt'

# load data
LIMIT = 80
dframe = pd.read_csv(in_filename, header=None, index_col=False)
sums = np.zeros((LIMIT,LIMIT))
sums[:,:] = np.nan

def coord_generator():
	yield 0,0
	for dist in xrange(1, LIMIT):
		# just change the col
		for c in xrange(dist):
			yield dist, c
		for r in xrange(dist):
			yield r, dist
		yield dist, dist

# for r,c in coord_generator():
# 	print("r=%d, c=%d" % (r,c))

# sums[0,0] = dframe.iloc[0,0]
for r,c in coord_generator():
	if np.isnan(sums[r,c]):
		sums[r,c] = dframe.iloc[r,c]
	else:
		sums[r,c] += dframe.iloc[r,c]
	if r+1 < LIMIT:
		if np.isnan(sums[r+1, c]):
			sums[r+1, c] = sums[r, c]
		elif sums[r+1, c] > sums[r, c]:
			sums[r+1, c] = sums[r, c]
	if c+1 < LIMIT:
		if np.isnan(sums[r, c+1]):
			sums[r, c+1] = sums[r, c]
		elif sums[r, c+1] > sums[r, c]:
			sums[r, c+1] = sums[r, c]
	# print(sums)
	# print("")

# print(sums)
print(sums[LIMIT-1,LIMIT-1])