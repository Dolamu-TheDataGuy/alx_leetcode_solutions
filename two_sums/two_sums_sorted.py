#!/usr/bin/python3
def binary_search(array, search_value):
    hi = len(array) - 1
    low = 0

    while low <= hi:
        mid = hi+low // 2
        if search_value > array[mid]:
            low = mid + 1
        elif search_value < array[mid]:
            hi = mid - 1
        else:
            return mid
    if array[hi] == search_value:
        return hi
    elif array[low] == search_value:
        return low
    else:
        print("Target not found")

def two_sums(array, target):
    for idx in range(len(array)):
        array[0]
        search_result = binary_search(array, target - array[idx])
        return [idx, search_result]

if __name__ == "__main__":
    print(two_sums([2,7,11,15], 9))