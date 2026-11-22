# тут собраны функции и стек для лабы

from .datasets import DATASET_KINDS, generate_dataset
from .fibonacci import fibonacci_iterative, fibonacci_recursive
from .sorting import insertion_sort, merge_sort
from .stack import Stack

__all__ = [
    "DATASET_KINDS",
    "Stack",
    "fibonacci_iterative",
    "fibonacci_recursive",
    "generate_dataset",
    "insertion_sort",
    "merge_sort",
]
