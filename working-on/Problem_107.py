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
import os

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
		self.assertEqual(150, compute_network_savings(training))

# Functions
def get_network_data():
	""" Parses and returns a network data file """
	# Initialize network
	network = []

	# Ensure that input data file exists, return empty network
	if not os.path.isfile(sys.argv[2]):
		return network

	# Parse input file into matrix form
	f = open(sys.argv[2])
		#for line in f:
		#	print line.strip().split(',')
	f.close()

	return network

def compute_network_savings(network):
	""" Compute savings between start network and optimal network """
	# Compute optimal network
	optimal = optimal_network_structure(network)

	# Saving is difference between size of old and new network
	return compute_network_weight(network) - compute_network_weight(optimal)

def optimal_network_structure(network):
	""" Compute minimum spanning tree of a network """
	return network

def compute_network_weight(network):
	""" Computes total weight of a network """
	return 0

# Main Function
if __name__ == '__main__':
	
	if len(sys.argv) > 1:
		# Parse input arguments: Training (Run test suite)
		if sys.argv[1] == "-test":
			suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_107)
			unittest.TextTestRunner(verbosity=2).run(suite)

		# Parse input arguments: Testing (Results)
		elif sys.argv[1] == "-run":
			# Get network matrix
			matrix = get_network_data()

			# Compute savings
			print "Distance saved:", compute_network_savings(matrix)

		# Invalid input format
		else:
			print "Please specify -test or -run argument"

	else:
		# Invalid input arguments message
		print "Expected input arguments: -[flag] path/to/datafile\n",\
				"Flags: test (runs test suite), run (performance)"
