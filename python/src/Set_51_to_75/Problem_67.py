#!/usr/bin/python
#
# Problem 67
# 
# Compute maximum sum in triangle with 100 rows. 

def triangle_main():
	""" Computes max sum path through 100-tier triangle """
	# Read triangle from file
	triangle = []
	f = open('data/data_67.txt')
	for line in f:
		triangle.append(map(int, line.strip().split()))
	f.close()

	# For each level, recompute each element as the best some of the last row
	for t in range(1, len(triangle)):
		# Initialize updated line
		update_line = []
		
		# First element automatically sums with previous first element
		update_line.append(triangle[t][0] + triangle[t-1][0])
		
		# Middle elements update to max sum of previous two elements
		for elem in range(1, len(triangle[t]) - 1):
			update_line.append(triangle[t][elem] + \
				max(triangle[t-1][elem], triangle[t-1][elem-1]))

		# Last elements are same
		update_line.append(triangle[t][t] + triangle[t-1][t-1])

		# Update line in triangle
		triangle[t] = update_line

	# Result = maximum member in last line
	print "Maximum sum:", max(triangle[99])

if __name__ == '__main__':
	triangle_main()
