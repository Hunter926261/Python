# Find the sum of digits.

def sum_digits(num: int) -> int:
    """
    Calculating sum of digit
    Args:
        num(int): Enter integer value
    Returns: 
        int: Sum of digit
    Raises:
        TypeError: When value is not integer
    """

    if not isinstance(num,int):
        raise TypeError("Value must be integer")

    num = abs(num)
    digit_sum = 0

    while num > 0:
        digit_sum += num%10
        num //= 10

    return digit_sum

print(sum_digits(123))