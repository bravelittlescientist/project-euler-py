#!/usr/bin/python
#
# Problem 29
# 
# How many distinct terms are in the sequence genrated by a^b
# for 2 <= a <= 100 and 2 <= b <= 100?

import unittest

class Test_Problem_29(unittest.TestCase):

	def test_sequence_for_range_2_to_5(self):
		""" For 2 <= a,b <= 5 there are 15 distinct terms in sequence """
		self.assertEqual(15, compute_distinct_terms_in_a_b_sequence(2,5))

def compute_distinct_terms_in_a_b_sequence(start,end):
	"""
	"""
	sequence = {}

	for base in range(start, end + 1):
		for power in range(start, end + 1):
			if base**power not in sequence:
				sequence[base**power] = 1

	return len(sequence)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_29)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Target: a^b for 2 <= a <= 100, 2 <= b <= 100"
	print "Result:", compute_distinct_terms_in_a_b_sequence(2,100)
