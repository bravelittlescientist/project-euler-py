#!/usr/bin/python
#
# Problem 81
#
# Find minimal path sum through grid  moving only down and right.

import unittest
import sys

class Test_Problem_81(unittest.TestCase):

	def test_compute_smaller_matrix_minimal_path_sum(self):
		""" Smaller test matrix min sum is 2427 """
		grid = read_grid()
		self.assertEqual(2427, compute_minimal_path(grid))

def read_grid():
	""" Read file of comma-separated numbers, return multidimensional grid """
	grid = []
	f = open(sys.argv[2])
	for line in f:
		grid.append([int(x) for x in line.strip().split(",")])
	f.close()
	return grid

def compute_minimal_path(grid):
	""" Computes min path through matrix from top-left to bottom-right """
	# Initialize minpath tracker for grid
	tracker = [[0 for c in range(len(grid))] for r in range(len(grid))]

	# Initialize top row, left column of tracker
	tracker[0][0] = grid[0][0]
	for position in range(1, len(grid)):
		# Left side of grid
		tracker[position][0] = tracker[position -1][0] + grid[position][0]

		# Top of grid
		tracker[0][position] = tracker[0][position -1] + grid[0][position]

	# Fill in tracker from top-left through each row
	for row in range(1, len(grid)):
		for col in range(1, len(grid)):

			# Best value for this spot is minimum of left and above
			tracker[row][col] = grid[row][col] + \
				min(tracker[row-1][col], tracker[row][col-1])
			
	# Optimal path is last value in tracker grid
	return tracker[len(grid) - 1][len(grid) - 1]

if __name__ == '__main__':
	# If test mode, run unittest
	if sys.argv[1] == '-test':
		suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_81)
		unittest.TextTestRunner(verbosity=2).run(suite)

	# Otherwise, run performanc test
	elif sys.argv[1] == '-run':
		print "Minimal Path Sum:", compute_minimal_path(read_grid())
