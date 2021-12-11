"""
Binary search algorithm implemented in python
"""


def callback(array):
    start = 0
    end = len(array) - 1

    return (start, end)


def binary_search(array, target, callback):  # assumes array is sorted
    start, end = callback(array)

    if start > end:
        return False

    mid_index = int((start + end) / 2)

    if array[mid_index] == target:
        return True

    if array[mid_index] > target:  # recurse left array
        return binary_search(array[start : mid_index - 1], target, callback)

    else:
        return binary_search(array[mid_index + 1 : end], target, callback)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    target = 4

    result = binary_search(array, target, callback)
    print(result)
