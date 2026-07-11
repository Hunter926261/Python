# Count the number of digits in an integer


def count_digit(num: int) -> int:
    """
    Return count of digit in integer
    Args:
        num(int): Enter integer
    Returns: 
        (int): count of digits
    """

    if not isinstance(num,int):
        raise TypeError("Input must be the integer")

    num = abs(num)
    count = 0

    if num == 0:
        return 1
    while num>0:
        count += 1
        num //= 10

    return count

print(count_digit(-123))