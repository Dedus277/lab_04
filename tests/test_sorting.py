import unittest
from random import Random

from algolab4 import insertion_sort, merge_sort


class SortingTests(unittest.TestCase):
    algorithms = (insertion_sort, merge_sort)

    def check_against_reference(self, values):
        expected = sorted(values)
        original = values.copy()
        for sort in self.algorithms:
            with self.subTest(sort=sort.__name__, values=values):
                result = sort(values)
                self.assertEqual(result, expected)
                self.assertIsNot(result, values)
                self.assertEqual(values, original)

    def test_edge_cases(self):
        for values in ([], [5], [-3, 0, 1, 3], [4, 2, 0, -2], [2, -1, 2, -1]):
            self.check_against_reference(values)

    def test_random_lists(self):
        rng = Random(42)
        for size in (0, 1, 2, 10, 100, 257):
            for _ in range(5):
                self.check_against_reference([rng.randint(-50, 50) for _ in range(size)])

    def test_invalid_types(self):
        for sort in self.algorithms:
            for values in ((1, 2), "12", None, [1, 2.5], [True], [1, "2"]):
                with self.subTest(sort=sort.__name__, values=values):
                    with self.assertRaises(TypeError):
                        sort(values)
