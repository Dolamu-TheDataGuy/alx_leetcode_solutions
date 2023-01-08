#!/usr/bin/python3
# Binary Search in python


def binary_search(arr, search_value, start):
    low = start
    high = len(arr) - 1
    while (low < high):
        mid  = (low + high) // 2
        if arr[mid] < search_value:
            low = mid + 1
        else:
            high = mid
    if (low ==  high and arr[low] == search_value):
        return low
    else:
        return -1


def two_sums(array, target):
    for idx in range(len(array)):
        search_result = binary_search(array, target - array[idx], idx + 1)
        if search_result != -1:
            return [idx + 1, search_result + 1]

if __name__ == "__main__":
    print(two_sums([2,7,11,15], 26))