# считаем числа фибоначчи циклом и рекурсией


def _check_n(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")


def fibonacci_iterative(n):
    _check_n(n)
    a = 0
    b = 1

    for _ in range(n):
        next_number = a + b
        a = b
        b = next_number

    return a


def _fib_step(steps_left, a, b):
    if steps_left == 0:
        return a
    return _fib_step(steps_left - 1, b, a + b)


def fibonacci_recursive(n):
    _check_n(n)
    # за один вызов двигаемся на одно число вперёд
    return _fib_step(n, 0, 1)
