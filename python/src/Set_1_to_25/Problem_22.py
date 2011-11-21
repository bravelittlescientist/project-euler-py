#!/usr/bin/python
#
# Problem 22
#
# Compute name scores of 46K text file by letters and position

import unittest

class Test_Problem_22(unittest.TestCase):

	def test_compute_basic_name_score(self):
		""" Compute name score, not factoring in position """
		self.assertEqual(53, base_name_score('COLIN'))

def base_name_score(name):
	""" Value of letters in name """
	return sum(map(lambda x: ord(x) - 96, list(name.lower())))

def compute_name_scores():
	""" Compute total scores of all names in list """
	# Initialize name list
	name_list = []

	# Read names fro mfile
	f = open('data/names.txt')
	for name in f:
		name_list.extend(name.strip().split(','))
	f.close()

	# Sort name list, remove quotation marks
	name_list = sorted(map(lambda x: x.strip('"'), name_list))

	# Compute position score
	total = 0
	position = 1
	for name in name_list:
		total += position * base_name_score(name)
		position += 1
	
	return total
	
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_Problem_22)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print "Total Score:", compute_name_scores()
