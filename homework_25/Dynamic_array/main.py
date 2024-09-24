from typing import Any, Iterator, List


class DynamicArray:
    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._size = 0
        self._array: List[Any] = [None] * capacity

    def _resize(self, new_capacity: int) -> None:
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, value: Any) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._array[self._size] = value
        self._size += 1

    def __getitem__(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._array[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._array[index] = value

    def __len__(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def __str__(self) -> str:
        return "[" + ", ".join(repr(self._array[i]) for i in range(self._size)) + "]"

    def __repr__(self) -> str:
        return f"DynamicArray([{', '.join(repr(self._array[i]) for i in range(self._size))}])"

    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        result = DynamicArray(self._size + other._size)
        for i in range(self._size):
            result.append(self._array[i])
        for i in range(other._size):
            result.append(other._array[i])
        return result

    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        for i in range(other._size):
            self.append(other._array[i])
        return self

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DynamicArray):
            return False
        if len(self) != len(other):
            return False
        for i in range(self._size):
            if self._array[i] != other._array[i]:
                return False
        return True

    def __lt__(self, other: 'DynamicArray') -> bool:
        return list(self) < list(other)

    def __le__(self, other: 'DynamicArray') -> bool:
        return list(self) <= list(other)

    def __gt__(self, other: 'DynamicArray') -> bool:
        return list(self) > list(other)

    def __ge__(self, other: 'DynamicArray') -> bool:
        return list(self) >= list(other)

    def __ne__(self, other: 'DynamicArray') -> bool:
        return not self == other

    def __iter__(self) -> Iterator[Any]:
        self._index = 0
        return self

    def __next__(self) -> Any:
        if self._index < self._size:
            result = self._array[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __hash__(self) -> int:
        raise TypeError("DynamicArray can't be hashed")

    def extend(self, values: List[Any]) -> None:
        for value in values:
            self.append(value)

    def pop(self) -> Any:
        if self._size == 0:
            raise IndexError("Pop from empty DynamicArray")
        value = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return value

    def remove(self, value: Any) -> None:
        for i in range(self._size):
            if self._array[i] == value:
                for j in range(i, self._size - 1):
                    self._array[j] = self._array[j + 1]
                self._array[self._size - 1] = None
                self._size -= 1
                return
        raise ValueError(f"{value} not found in DynamicArray")
