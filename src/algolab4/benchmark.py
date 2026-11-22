# замеряем время обеих сортировок

import argparse
import csv
from statistics import median
from time import perf_counter_ns

from .datasets import DATASET_KINDS, generate_dataset
from .sorting import insertion_sort, merge_sort

SIZES = (100_000, 1_000_000, 10_000_000)
REPEATS = 5
QUADRATIC_DATASETS = ("random", "reverse", "duplicates")# типы списков, на которых сортировка вставками медленная
SLOW_INSERTION_MIN_SIZE = 100_000


def _write_result(writer, kind, size, name, seed, times):
    row = [kind, size, name, seed]
    if times:
        row += ["measured", len(times), round(median(times), 6)]
        for time in times:
            row.append(round(time, 6))
    else:
        row += ["skipped_quadratic", 0, ""]
        row += [""] * REPEATS
    writer.writerow(row)


def run_benchmark(output, seed, include_slow=False):
    with open(output, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        header = ["dataset", "size", "algorithm", "seed", "status", "repeats", "median_ms"]
        for run in range(1, REPEATS + 1):
            header.append("run_" + str(run) + "_ms")
        writer.writerow(header)

        for size in SIZES:
            for kind in DATASET_KINDS:
                source = generate_dataset(kind, size, seed=seed)
                skip_insertion = False
                if kind in QUADRATIC_DATASETS and size >= SLOW_INSERTION_MIN_SIZE:
                    skip_insertion = not include_slow

                insertion_times = []
                merge_times = []
                for repeat in range(REPEATS):
                    order = ["insertion_sort", "merge_sort"]
                    if repeat % 2 == 1:
                        order.reverse()

                    for name in order:
                        if name == "insertion_sort" and skip_insertion:
                            continue

                        # копируем список до замера
                        numbers = source.copy()
                        if name == "insertion_sort":
                            start = perf_counter_ns()
                            result = insertion_sort(numbers)
                            finish = perf_counter_ns()
                            insertion_times.append((finish - start) / 1_000_000)
                        else:
                            start = perf_counter_ns()
                            result = merge_sort(numbers)
                            finish = perf_counter_ns()
                            merge_times.append((finish - start) / 1_000_000)

                        # освобождаем память после замера
                        del result
                        del numbers

                _write_result(writer, kind, size, "insertion_sort", seed, insertion_times)
                _write_result(writer, kind, size, "merge_sort", seed, merge_times)
                del source
                file.flush()


def main():
    parser = argparse.ArgumentParser(description="Сравнение времени двух сортировок.")
    parser.add_argument("--output", default="benchmark.csv")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--include-slow",
        action="store_true",
        help="выполнить также очень долгие замеры сортировки вставками",
    )
    args = parser.parse_args()
    run_benchmark(args.output, seed=args.seed, include_slow=args.include_slow)
    print("CSV:", args.output)


if __name__ == "__main__":
    main()
