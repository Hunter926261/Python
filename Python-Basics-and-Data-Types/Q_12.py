# Check whether a number is a Perfect Number.

# In mathematics, a perfect number is a positive integer that is exactly equal to the sum of its proper positive divisors (all its factors excluding the number itself). For example, the proper divisors of 6 are 1, 2, and 3, and \(1 + 2 + 3 = 6\).

import math

def check_perfect_number(num: int) -> bool:
    """
    Checking weather number is perfect number or not

    Args:
        num(int): Enter a positive integer
    Returns:
        bool: True if perfect number and False if not.

    Raises:
        TypeError: When value is not integer
        ValueError: When value is negative
    """

    total = 0
    if not isinstance(num,int):
        raise TypeError("Value must be positive integer")
    
    if num < 0:
        raise ValueError("Value must be positive")
    
    if num < 1:
        return False
        
    for i in range(1,num):
        if num%i == 0:
            total += i
    return total == num

print(check_perfect_number(6))