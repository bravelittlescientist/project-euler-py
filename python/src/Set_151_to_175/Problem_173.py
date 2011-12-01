#!/usr/bin/python
#
# Problem 173: Square Laminae
# 
# We shall define a square lamina to be a square outline with a square "hole" 
# so that the shape possesses vertical and horizontal symmetry. For example, 
# using exactly thirty-two square tiles we can form two different square 
# laminae:
#
# ######	#########
# ######	#		#
# ##  ##	#		#
# ##  ##	#		#
# ######	#		#
# ######	#		#
#			#		#
#			#		#
#			#########
#
# With one-hundred tiles, and not necessarily using all of the tiles at 
# one time, it is possible to form forty-one different square laminae.
#
# Using up to one million tiles, how many different square laminae 
# can be formed?

import unittest
import sys

class Test_Problem_173(unittest.TestCase):

	def test_exact_quantity_of_tiles(self):
		""" Using exactly 32 tiles, only 2 laminae can be formed """
		self.assertEqual(2, count_laminae(32, exact=True))

	def test_compute_toy_laminae_problems(self):
		""" Compute laminae using 100, 8, 12 """
		self.assertEqual(41, count_laminae(100))		
		self.assertEqual(2, count_laminae(12))
		self.assertEqual(1, count_laminae(8))

	def test_compute_lamina_must_have_hole(self):
		""" Lamina must have at least 8 tiles to have a square hole """
		self.assertEqual(0, count_laminae(7))

def count_laminae(tiles_available, exact=False):
	""" Compute square laminae given (possibly exact) square tiles

	@param tiles_available is the tiles available, inclusive
	@param exact, default False, is whether all tiles must be used at once
	"""
	return -1

if __name__ == '__main__':
	
	# Check command line arguments
	if len(sys.argv) < 2:
		print "Run with -test or -run flag"

	# To run test suite
	elif sys.argv[1] == '-test':
		suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_173)
		unittest.TextTestRunner(verbosity=2).run(suite)

	# To check actual result
	elif sys.argv[1] == '-run':
		print "Using up to 1 million tiles, quantity laminae:",\
			count_laminae(999999)
