#!/usr/bin/python
#
# Problem 56
#
# Considering natural numbers of the form a^b, where a, b < 100, what is
# the maximum digital sum?

import unittest

class Test_Problem_56(unittest.TestCase):
	
	def test_compute_digital_sum(self):
		""" Compute sum of digits of a number """
		self.assertEqual(2, digital_sum(2))
		self.assertEqual(1, digital_sum(10**100))
		self.assertEqual(6, digital_sum(42))

	def test_max_digital_sum(self):
		""" 9, for natural numbers of the form a^b, where a,b < 4 """
		self.assertEqual(9, max_digital_sum(4))

def digital_sum(n):
	""" Compute sum of digits in n """
	return sum(map(int, list(str(n))))

def max_digital_sum(limit):
	""" max digital sum of natural numbers of form a^b, where a,b < limit """
	maximum = 0

	for a in range(1,limit):
		for b in range(1, limit):
			maximum = max(maximum, digital_sum(a**b))

	return maximum

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_56)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Maximum digital sum for a^b, a,b < 100:", max_digital_sum(100)
