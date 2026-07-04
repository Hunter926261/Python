# Find the largest digit in a number.

def largest_digit(num: int) -> int:
    """
    Returning the largest digit from number
    Args: 
        num(int): Enter integer value
    Returns:
        int: Largest digit from number
    Raises: 
        TypeError: When value is not integer 
    """

    if not isinstance(num,int):
        raise TypeError("Value must be integer")
    
    num = abs(num)
    largest_num = -1

    if num == 0:
        return 0

    while num > 0:
        if num%10 > largest_num:
            largest_num = num%10
        num //= 10

    return largest_num

print(largest_digit(10))