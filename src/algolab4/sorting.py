# тут две сортировки, вставками и слиянием


def _copy_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("values must be a list of integers")
    for number in numbers:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("values must contain integers")
    return numbers.copy()


def insertion_sort(values):
    numbers = _copy_numbers(values)
    for i in range(1, len(numbers)):
        number = numbers[i]
        j = i
        # освобождаем место для числа, сдвигая вправо всё, что больше него
        while j > 0 and numbers[j - 1] > number:
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = number
    return numbers


def merge_sort(values):
    return _split_and_merge(_copy_numbers(values))


def _split_and_merge(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = _split_and_merge(numbers[:middle])
    right = _split_and_merge(numbers[middle:])

    # если половины уже идут по порядку, просто склеиваем их
    if left[-1] <= right[0]:
        return left + right
    if right[-1] < left[0]:
        return right + left

    result = []
    i = 0
    j = 0
    left_size = len(left)
    right_size = len(right)

    # сравниваем первые из оставшихся чисел и берём меньшее
    while i < left_size and j < right_size:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # когда одна половина закончилась, дописываем остаток второй
    result.extend(left[i:])
    result.extend(right[j:])
    return result
