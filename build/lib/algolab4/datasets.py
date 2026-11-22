# делаем разные списки для проверки сортировок

from random import Random

DATASET_KINDS = ("random", "sorted", "reverse", "nearly_sorted", "duplicates")


def generate_dataset(kind, size, *, seed=None):
    if kind not in DATASET_KINDS:
        raise ValueError(f"unknown dataset kind: {kind!r}")
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be non-negative")

    if kind == "sorted":
        return list(range(size))
    if kind == "reverse":
        return list(range(size - 1, -1, -1))

    rng = Random(seed)
    if kind == "nearly_sorted":
        numbers = list(range(size))
        if size >= 2:
            # берём соседние пары так, чтобы ни одно число не поменять дважды
            pairs = range(0, size - 1, 2)
            swaps = max(1, size // 100)
            for i in rng.sample(pairs, swaps):
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        return numbers

    limit = size
    if kind == "duplicates":
        limit = 2
    numbers = []
    for _ in range(size):
        numbers.append(rng.randint(-limit, limit))
    return numbers
