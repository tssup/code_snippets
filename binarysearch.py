"""
Binary search algorithm implemented in python
"""


def binary_search(array, start, end, target):  # assumes array is sorted
    if start > end:
        return False

    mid_index = int((start + end) / 2)

    if array[mid_index] == target:
        return True

    if array[mid_index] > target:  # recurse left array
        return binary_search(array, start, mid_index - 1, target)

    else:
        return binary_search(array, mid_index + 1, end, target)


if __name__ == "__main__":
    # array = [1, 2, 3, 4, 5, 6]
    # start = 0
    # end = len(array) - 1
    # target = 4

    # result = binary_search(array, start, end, target)
    # print(result)
