#!/usr/bin/python
#
# Problem 107: Find maximum savings in redundant network
#
# Given an undirected network of vertices and edges, represented as a matrix,
# remove edges to save edge weight while keeping all vertices connected.
# 
# Goal: Compute maximum saving by removing redundant edges.

import unittest
import sys

# Test Suite
class Test_Problem_107(unittest.TestCase):
	
	# Computing total network weight
	def test_compute_start_weight_of_training_network(self):
		""" Training network has total weight of 243 when redundant """
		training = get_network_data()
		self.assertEqual(243, compute_network_weight(training))

	def test_compute_end_weight_of_training_network(self):
		""" Training network has total weight of 93 when not redundant """
		training = get_network_data()
		training_optimized = optimal_network_structure(training)
		self.assertEqual(93, compute_network_weight(training_optimized))

	# Computing total savings
	def test_compute_training_savings(self):
		""" Training network can save 150 weight removing redundant edges """
		training = get_network_data()
		training_optimal = optimal_network_structure(training)
		self.assertEqual(150, compute_network_weight(training) - \
								compute_network_weight(training_optimal))

# Functions
def get_network_data():
	""" Parses and returns a network data file """
	# Initialize network
	network = []

	# Check for valid arguments, and parse network if possible
	if sys.argv[1] == '-train' or sys.argv[1] == '-test':
		
		# Parse input file into matrix form
		f = open(sys.argv[2])
			#for line in f:
			#	print line.strip().split(',')
		f.close()

	return network

# Main Function
if __name__ == '__main__':
	
	if len(sys.argv) > 1:
		# Parse input arguments: Training (Run test suite)
		if sys.argv[1] == "-train":
			pass

		# Parse input arguments: Testing (Results)
		elif sys.argv[2] == "-test":
			pass

		# Invalid input format
		else:
			print "Please specify -test or -train dataset"

	else:
		# Invalid input arguments message
		print "Expected input arguments: -[flag] path/to/datafile\n",\
				"Flags: train (runs test suite), test (performance)"
