def two_sums(array, target):
    """
    Given an array of integers nums and an integer target, return indices 
    of the two numbers such that they add up to target.
    
    Method of solution:
    This method of solution uses a dictionary to look up the values
    to see which value equals to (target - x).
    
     
    Time Complexity => O(n)
    Space Complexity => O(n)
    """
    d = {}
    for (idx,value) in enumerate(array):
        rem = target - value
        if rem in d.keys():
            return [d[rem], idx]
        else:
            d[value] = idx
    
print(two_sums([2,7,8,11,1,2], 9))