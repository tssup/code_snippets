"""
merge sort algo implemented in python
"""


def merge_sort(array):
    if len(array) < 2:
        return array

    mid_index = int(len(array) / 2)
    end = len(array)

    left_array = array[0:mid_index]
    right_array = array[mid_index:end]

    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(left_array, right_array):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            result.append(left_array[left_index])
            left_index += 1

        else:
            result.append(right_array[right_index])
            right_index += 1

    result.extend(left_array[left_index:])
    result.extend(right_array[right_index:])

    return result


if __name__ == "__main__":
    print(merge_sort([1, 8, 9, 3, 100, 8]))
