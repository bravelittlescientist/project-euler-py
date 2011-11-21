#!/usr/bin/python
#
# Problem 55
# Compute Lychrel numbers below 10,000
#
# Some numbers can be reversed and added, to become palindromic.
# e.g., 47 + 74 = 121. Sometimes this takes a few iterations:
# 349 + 943 = 1292
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
# Lychrel numbers never become palindromes through this process. Assume
# that any number below 10,000 will either find a palindrome in less than
# fifty iterations, or never. By definition, single-digit numbers (>= 0)
# are palindromic

import unittest

class Test_Problem_55(unittest.TestCase):
	
	def test_compute_is_palindromic(self):
		""" Check if is_palindromic computes correctly """
		self.assertFalse(is_palindromic(1234))
		self.assertTrue(is_palindromic(1221))
		self.assertTrue(is_palindromic(34543))
		self.assertTrue(is_palindromic(0))
		self.assertTrue(is_palindromic(3))
		self.assertFalse(is_palindromic(123))

	def test_compute_reverse_and_sum(self):
		""" Check that sum and reverse provides correct sum """
		self.assertEqual(121, reverse_and_sum(47))
		self.assertEqual(1292, reverse_and_sum(349))
		self.assertEqual(4213, reverse_and_sum(1292))
		self.assertEqual(7337, reverse_and_sum(4213))

	def test_196_is_a_lychrel_number(self):
		self.assertEqual(1, compute_quantity_lychrels_in_range(196,197))

def is_palindromic(n):
	""" Compute if number is palindromic """
	n_string = str(n)

	# Single-digit numbers are palindromic
	if n >= 0 and len(n_string) == 1:
		return True

	# Depending on if length is even or odd, compute palindrome
	first_half = n_string[:len(n_string)/2]
	if not len(n_string) % 2:
		second_half = n_string[len(n_string)/2:]
	else:
		second_half = n_string[(len(n_string)/2) + 1:]
	return first_half == second_half[::-1]

def reverse_and_sum(n):
	""" Reverse number and sum reverse with n """
	reverse = int(str(n)[::-1])
	return n + reverse

def compute_quantity_lychrels_in_range(low, high):
	""" Compute quantity of Lychrel numbers above-including low, below high """
	lychrel = 0

	# Iterate through numbers in range
	for i in range(low, high):
		check_num = i
		found = 0	
		turn_counter = 1
		while turn_counter < 50 and not found:
			# Check if reversed and summed is palindromic
			check_num = reverse_and_sum(check_num)
			if is_palindromic(check_num):
				found = 1

			# Update counter
			turn_counter += 1
	
		if not found: 
			lychrel += 1

	return lychrel

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_55)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Number of Lychrels below 10,000:",\
		compute_quantity_lychrels_in_range(0,10000)
