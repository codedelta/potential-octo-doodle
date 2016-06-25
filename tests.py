import unittest
from .primes import is_prime


class PrimesTestCase(unittest.TestCase):
	def test(self):
		self.assertTrue(is_prime(5))

	def test_negative_number(self):
		for index in range(-1, -10, -1):
			self.assertFalse(is_prime(index),msg='{} should not be determined to be prime'.format(index))

if __name__ == "__main__":
	unittest.main()