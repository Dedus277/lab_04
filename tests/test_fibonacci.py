import sys
import unittest

from algolab4 import fibonacci_iterative, fibonacci_recursive


class FibonacciTests(unittest.TestCase):
    def test_known_values(self):
        expected = {0: 0, 1: 1, 2: 1, 3: 2, 10: 55, 50: 12_586_269_025}
        for fibonacci in (fibonacci_iterative, fibonacci_recursive):
            for n, answer in expected.items():
                with self.subTest(function=fibonacci.__name__, n=n):
                    self.assertEqual(fibonacci(n), answer)

    def test_invalid_indices(self):
        for fibonacci in (fibonacci_iterative, fibonacci_recursive):
            with self.subTest(function=fibonacci.__name__):
                with self.assertRaises(ValueError):
                    fibonacci(-1)
                for value in (True, 2.0, "2", None):
                    with self.subTest(value=value), self.assertRaises(TypeError):
                        fibonacci(value)

    def test_recursive_call_obeys_python_limit(self):
        with self.assertRaises(RecursionError):
            fibonacci_recursive(sys.getrecursionlimit())
