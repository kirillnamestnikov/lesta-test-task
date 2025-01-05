import time


class Node:
    def __init__(self, v: int, n=None):
        self.value = v
        self.next = n


class NodeCyclicBuffer:
    def __init__(self, capacity: int):
        self.last = None
        self.capacity = capacity
        self.size = 0

    def push(self, value: int) -> None:
        if self.is_full():
            raise RuntimeError("Buffer is full")
        if self.is_empty():
            temp = Node(value)
            temp.next = temp
            self.last = temp
        else:
            temp = Node(value)
            temp.next = self.last.next
            self.last.next = temp
            self.last = temp
        self.size += 1
            
    def pop(self) -> int:
        if self.is_empty():
            raise RuntimeError("Buffer is empty")
        temp = self.last.next.value
        if self.size == 1:
            self.last = None
        else:
            self.last.next = self.last.next.next
        self.size -= 1
        return temp

    def get_front(self) -> int:
        if self.is_empty():
            raise RuntimeError("Buffer is empty")
        return self.last.next.value

    def get_last(self) -> int:
        if self.is_empty():
            raise RuntimeError("Buffer is empty")
        return self.last.value

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def get_size(self) -> int:
        return self.size


class ShiftCyclicBuffer:
    def __init__(self, capacity: int) -> None:
        self.front = 0
        self.end = 0
        self.size = 0
        self.capacity = capacity
        self.buf = list(range(0, capacity))

    def push(self, value: int) -> None:
        if self.end >= self.capacity:
            self.end = 0
        if self.__is_pointers_equal():
            self.__shift_left()
        self.buf[self.end] = value
        self.end += 1
        if (self.size < self.capacity):
            self.size += 1

    def __is_pointers_equal(self) -> bool:
        return (self.size != 0) and (self.front == self.end)
    
    def __shift_left(self) -> None:
        if self.front + 1 < self.capacity:
            self.front += 1
        else:
            self.front = 0

    def pop(self) -> int:
        if self.size == 0:
            raise RuntimeError("Can not pop an empty buffer")
        elem = self.buf[self.front]
        self.size -= 1
        self.__shift_left()
        return elem

    def get_front(self) -> int:
        if self.size == 0:
            raise RuntimeError("Buffer is empty")
        elem = self.buf[self.front]
        return elem

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return (self.get_size() == 0)


def main() -> None:
    start = time.perf_counter()
    buffer = ShiftCyclicBuffer(capacity=1_000_000)
    for num in range(1, 1_000_001):
        buffer.push(num)
    print(buffer.get_size())
    for _ in range(buffer.get_size()):
        buffer.pop()
    print(buffer.get_size())
    print("Время работы первого буфера:", time.perf_counter() - start)
    start2 = time.perf_counter()
    buffer2 = NodeCyclicBuffer(capacity=1_000_000)
    for num in range(1, 1_000_001):
        buffer2.push(num)
    print(buffer2.get_size())
    for _ in range(buffer2.get_size()):
        buffer2.pop()
    print(buffer2.get_size())
    print("Время работы второго буфера:", time.perf_counter() - start2)

if __name__ == "__main__":
    main()

