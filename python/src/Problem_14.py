#!/usr/bin/python
#
# Problem 14
# 
# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
#
#  It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# Note: Once the chain starts the terms are allowed to go above one million.

import unittest

class Test_Problem_14(unittest.TestCase):

	def test_get_next_sequence_step_halves_even_value(self):
		""" If n is even, next step in sequence is n/2 """
		self.assertEqual(3, get_next_sequence_step(6))

	def test_get_next_sequence_step_triples_odd_value_adds_1(self):
		""" If n is odd, next step in sequence is 3n + 1 """
		self.assertEqual(10, get_next_sequence_step(3))

	def test_get_correct_start_n_for_longest_chain(self):
		""" Correct starting points with upper bounds of 14, 6 """
		self.assertEqual(9, get_longest_sequence_length_start_number_under(14))
		self.assertEqual(3, get_longest_sequence_length_start_number_under(6))

def get_next_sequence_step(n):
	""" 
	Returns next step of Collatz sequence
	n -> n/2 (n is even)
	n -> 3n + 1 (n is odd)
	"""
	if not n % 2:
		return n/2
	else:
		return 3*n + 1

def get_longest_sequence_length_start_number_under(n):
	"""
	"""
	# Track path lengths to avoid extra operations
	path_length_tracker = {}
	
	# Track start point for max path length
	start = 0	
	max_path_length = 0

	# n is upper bound of available sequence start points
	for i in range(2, n):
		result = i
		counter = 1

		# Map each sequence until it reaches a 
		while result != 1:
			result = get_next_sequence_step(result)
			if result in path_length_tracker:
				counter += path_length_tracker[result]
				result = 1
			else:
				counter += 1
			
			# Update path length tracker
			path_length_tracker[i] = counter

			# Update max path length and start point
			if counter > max_path_length:
				max_path_length = counter
				start = i

	return start

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_14)
	unittest.TextTestRunner(verbosity=2).run(suite)

	target = 1000000
	print "Longest chain start point under 1 million", get_longest_sequence_length_start_number_under(target)
