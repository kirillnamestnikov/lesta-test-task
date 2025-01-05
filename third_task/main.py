from random import randint
import time

def merge(left: list[int], right: list[int]) -> list[int]:
    res = []
    left_index, right_index = 0, 0
    left_size, right_size = len(left), len(right)
    size = left_size + right_size
    for _ in range(size):
        if left_index < left_size and right_index < right_size:
            if left[left_index] <= right[right_index]:
                res.append(left[left_index])
                left_index += 1
            else:
                res.append(right[right_index])
                right_index += 1
        elif left_index == left_size:
            res.append(right[right_index])
            right_index += 1
        elif right_index == right_size:
            res.append(left[left_index])
            left_index += 1
    return res

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        mid_index = len(arr) // 2
        left = merge_sort(arr[:mid_index])
        right = merge_sort(arr[mid_index:])
    return merge(left, right)

def main() -> None:
    arr = []
    for _ in range(100):
        arr.append(randint(1, 1_000_000))
    start = time.perf_counter()
    arr = merge_sort(arr)
    print(time.perf_counter() - start)
    print(arr)

if __name__ == "__main__":
    main()
