import unittest

from fibonacci_message_encoding import fibonacci


# Fibonacci values pulled from https://oeis.org/A000045/list
# n = [0, 38]
FIBONACCI_VALUES = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
                    4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
                    832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
                    39088169]


class TestAlgorithmsFibonacci(unittest.TestCase):

    def test_fibonacci_equation_start_0(self):
        for i, FIBO_VALUE in enumerate(FIBONACCI_VALUES):
            self.assertEqual(fibonacci._fibonacci_number_start_0(i), FIBO_VALUE)

    def test_fibonacci_equation_start_1(self):
        for i, FIBO_VALUE in enumerate(FIBONACCI_VALUES[1:]):
            self.assertEqual(fibonacci._fibonacci_number_start_1(i), FIBO_VALUE)