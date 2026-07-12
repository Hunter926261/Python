# Check if a number is a power of 2 using bitwise

# Formula: n & (n - 1)
# Where n is number to check

def check_power_2(n: int) -> bool:
    """
    Check if a number is a power of 2 using bitwise
    Args:
        n(int): Enter non-negative integer
    Returns:
        bool: True if number is power of 2 else False
    """

    if not isinstance(n,int):
        raise TypeError("n must be non-negative integer")
    
    if n < 0:
        raise ValueError("n must be non-negative integer")
    
    if n == 0:
        return False

    return n & (n-1) == 0

print(check_power_2(16))
print(check_power_2(0))