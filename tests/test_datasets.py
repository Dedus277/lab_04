import unittest

from algolab4 import DATASET_KINDS, generate_dataset


class DatasetTests(unittest.TestCase):
    def test_sizes(self):
        for kind in DATASET_KINDS:
            for size in (0, 1, 2, 100):
                with self.subTest(kind=kind, size=size):
                    values = generate_dataset(kind, size, seed=42)
                    self.assertEqual(len(values), size)
                    self.assertTrue(all(type(value) is int for value in values))

    def test_seed_reproducibility(self):
        for kind in DATASET_KINDS:
            with self.subTest(kind=kind):
                first = generate_dataset(kind, 200, seed=42)
                second = generate_dataset(kind, 200, seed=42)
                self.assertEqual(first, second)
                self.assertIsNot(first, second)

    def test_different_seeds_change_randomized_datasets(self):
        for kind in ("random", "nearly_sorted", "duplicates"):
            with self.subTest(kind=kind):
                self.assertNotEqual(
                    generate_dataset(kind, 200, seed=42),
                    generate_dataset(kind, 200, seed=91),
                )

    def test_distribution_properties(self):
        ascending = list(range(200))
        self.assertEqual(generate_dataset("sorted", 200), ascending)
        self.assertEqual(generate_dataset("reverse", 200), ascending[::-1])
        nearly_sorted = generate_dataset("nearly_sorted", 200, seed=42)
        self.assertEqual(sorted(nearly_sorted), ascending)
        inversions = sum(left > right for left, right in zip(nearly_sorted, nearly_sorted[1:]))
        self.assertEqual(inversions, 2)
        duplicates = generate_dataset("duplicates", 200, seed=42)
        self.assertTrue(set(duplicates) <= {-2, -1, 0, 1, 2})
        self.assertLess(len(set(duplicates)), len(duplicates))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_dataset("unknown", 1)
        with self.assertRaises(ValueError):
            generate_dataset("random", -1)
        with self.assertRaises(TypeError):
            generate_dataset("random", 1.5)
