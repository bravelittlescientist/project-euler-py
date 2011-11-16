#!/usr/bin/python
#
# Problem 45
#
# Triangle, pentagonal, and hexagonal numbers are generated by the
# following formulae:
# Triangle		T(n) = n(n+1)/2
# Pentagonal	P(n) = n(3n-1)/2
# Hexagonal		H(n) = n(2n-1)
# T(285) = P(165) = H(143) = 40755
# Find the next triangle number that is also pentagonal and hexagonal

import unittest

class Test_Problem_45(unittest.TestCase):

	def test_compute_triangle_numbers(self):
		""" Accurate compute triangle series numbers """
		self.assertEqual(1, triangle_number(1))
		self.assertEqual(3, triangle_number(2))
		self.assertEqual(6, triangle_number(3))
		self.assertEqual(10, triangle_number(4))
		self.assertEqual(15, triangle_number(5))
		self.assertEqual(40755, triangle_number(285))

	def test_compute_pentagonal_numbers(self):
		self.assertEqual(1, pentagonal_number(1))
		self.assertEqual(5, pentagonal_number(2))
		self.assertEqual(12, pentagonal_number(3))
		self.assertEqual(22, pentagonal_number(4))
		self.assertEqual(35, pentagonal_number(5))
		self.assertEqual(40755, pentagonal_number(165))

	def test_compute_hexagonal_numbers(self):
		self.assertEqual(1, hexagonal_number(1))
		self.assertEqual(6, hexagonal_number(2))
		self.assertEqual(15, hexagonal_number(3))
		self.assertEqual(28, hexagonal_number(4))
		self.assertEqual(45, hexagonal_number(5))
		self.assertEqual(40755, hexagonal_number(143))
	
	def test_first_triangle_pentagonal_hexagonal_n(self):
		""" Computes T(285) = P(165) = H(143) = 40755 """
		self.assertEqual(40755, compute_next_triangle_pentagonal_hexagonal_n([1]))

def triangle_number(n):
	""" Compute triangle n(n+1)/2 """
	return n*(n+1)/2

def pentagonal_number(n):
	""" Compute pentagonal n(3n-1)/2 """
	return n*(3*n - 1)/2

def hexagonal_number(n):
	""" Compute hexagonal n(2n-1) """
	return n*(2*n - 1)

def compute_next_triangle_pentagonal_hexagonal_n(covered=[]):
	""" Computes next n which is triangle, pentagonal and hexagonal

	Optionally, covered will allow prevoiusly discovered numbers
	to be removed from consideration.
	"""
	# Initializations
	triangles = {}
	pentagonals = {}
	hexagonals = {}
	n = 1
	
	# Track triangles while computing others, since they grow quickly with n
	while True:
		# Compute next set of numbers
		pentagonals[pentagonal_number(n)] = n
		hexagonals[hexagonal_number(n)] = n
		t = triangle_number(n)

		# Check for triplets
		if t in pentagonals and t in hexagonals and t not in covered:
			return t
		n += 1

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_45)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Result:", compute_next_triangle_pentagonal_hexagonal_n([1,40755])