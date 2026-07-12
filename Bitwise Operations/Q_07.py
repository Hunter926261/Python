# check whether the k-th bit of a number is set (1)

# Formula: n & (1 << k)
# Where:
# n → Number
# k → Bit position (0-based indexing from the right)
# 1 << k → Creates a mask with only the k-th bit set.

def check_kth_bit(num: int, k: int) -> bool:
    """
    check whether the k-th bit of a number is set (1)
    Args:
        num(int): Enter non-integer value
        k(int): Enter non-integer value
    Returns: 
        bool: True if k-th bit of a number is set (1) else False
    """

    if not all(isinstance(x,int) for x in (num,k)):
        raise TypeError("Number & k must be the non-negative integer")
    
    if any(x < 0 for x in (num,k)):
        raise ValueError("Number & k must be the non-negative integer")

    return num & (1 << k) != 0

print(check_kth_bit(11,2))
print(check_kth_bit(10,3))