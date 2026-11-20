# стек хранит элементы в обычном списке

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        # снимаем верхний элемент, на пустом стеке будет ошибка
        return self._items.pop()

    def peek(self):
        # смотрим на верхний элемент, он остаётся в стеке
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return len(self._items) > 0
