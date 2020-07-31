# pylint
# pyflakes


# AutoPEP 8


import unittest
import test_main

class TestMain(unittest.TestCase):
	def setUp(self):
		print('about to test a function')

	def test_do_stuff(self):
		'''Test 1'''
		test_param = 10
		result = test_main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_param = 'ssljslj'
		result = test_main.do_stuff(test_param)
		self.assertTrue(isinstance(result, ValueError))

	def test_to_stuff3(self):
		test_param = None
		result = test_main.do_stuff(test_param)
		self.assertEqual(result, 'please enter number')

	def test_to_stuff4(self):
		test_param = ''
		result = test_main.do_stuff(test_param)
		self.assertEqual(result, 'please enter number')

	def tearDown(self):
		print('cleaning up')

if __name__ == '__main__':
	unittest.main()
