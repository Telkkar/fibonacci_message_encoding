import unittest

from fibonacci_message_encoding import fibonacci


# Fibonacci values pulled from https://oeis.org/A000045/list
# n = [0, 38]
FIBONACCI_VALUES = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
                    4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
                    832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
                    39088169]

# Following numbers are pulled from
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
NUMBER_70 = 190392490709135
NUMBER_71 = 308061521170129
NUMBER_72 = 498454011879264

NUMBER_300 = 222232244629420445529739893461909967206666939096499764990979600


class TestAlgorithmsFibonacci(unittest.TestCase):

    def test_fibonacci_equation_start_0_first_39(self):
        for i, FIBO_VALUE in enumerate(FIBONACCI_VALUES):
            self.assertEqual(fibonacci._fibonacci_number_start_0(i), FIBO_VALUE)

    def test_fibonacci_equation_start_1_first_39(self):
        for i, FIBO_VALUE in enumerate(FIBONACCI_VALUES[1:]):
            self.assertEqual(fibonacci._fibonacci_number_start_1(i), FIBO_VALUE)

    def test_fibonacci_equation_start_1_number_70(self):
        self.assertEqual(fibonacci._fibonacci_number_start_0(70), NUMBER_70)

    def test_fibonacci_equation_start_1_number_71(self):
        self.assertEqual(fibonacci._fibonacci_number_start_0(71), NUMBER_71)

    def test_fibonacci_equation_start_1_number_72(self):
        self.assertEqual(fibonacci._fibonacci_number_start_0(72), NUMBER_72)

    def test_fibonacci_equation_start_1_number_300(self):
        self.assertEqual(fibonacci._fibonacci_number_start_0(300), NUMBER_300)