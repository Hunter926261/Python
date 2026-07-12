# Find missing number using XOR.

# The XOR method is one of the most efficient ways to find a missing number in an array containing numbers from 1 to n with exactly one number missing.

# Algorithm
# XOR all numbers from 1 to n.
# XOR all elements of the array.
# XOR the two results.
# The remaining value is the missing number.

def find_missing_num(nums: list[int],n: int) -> int:
    """
    Find the missing value from array of integer
    Args:
        nums(list): Enter the list of integer of having only one or non missing value
        n: If list of 1-n, Enter the value of n
    Returns:
        int: missing value from the array 
    """

    if not all(isinstance(x,int) for x in nums):
        raise TypeError("list must contain non-negative integer")
    
    if not isinstance(n,int):
        raise TypeError("n must be positive integer")
    
    if n < 0:
        raise ValueError("n must be positive integer")
    
    if any(x < 0 for x in nums):
        raise ValueError("list must contain non-negative integer")
    
    if len(nums) != (n-1):
        raise ValueError("Array at most contains 1 missing number")
    
    # elements in array should not be greater than n
    if any(x > n for x in nums):
        raise ValueError("Value in array must be smaller or equal to n")
    
    if len(nums) != len(set(nums)):
        raise ValueError("Elements in nums must be unique")

    xor_all = 0
    xor_array = 0

    # XOR of 1 - n
    for i in range(1,n+1):
        xor_all ^= i

    # XOR of array (nums)
    for i in nums:
        xor_array ^= i

    return xor_all ^ xor_array


nums = [1,2,3,4,6]
n = 6

print(find_missing_num(nums,n))