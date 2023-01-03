def two_sums(array, target):
    """
    Given an array of integers nums and an integer target, return indices 
    of the two numbers such that they add up to target.

    Method of solution:
    Loop through each element x of the array and find if there is 
    another value that equals (target - x). Finding another value
    requires another loop on the array.

    
    Time Complexity => O(n^2)
    Space Complexity => O(n)

    """
    for i in range(len(arr)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]
            else:
                return []
