# Find the last digit of a number

def last_digit(num: int) -> int:
    """
    Return the last digit of number
    Args:
        num(int): Input integer
    Returns: 
        int: last digit of integer
    Raises: 
        TypeError: If num is not integer
    """
    
    if not isinstance(num,int):
        raise TypeError("Input must be the integer")
    
    return abs(num)%10

print(last_digit(9644))
