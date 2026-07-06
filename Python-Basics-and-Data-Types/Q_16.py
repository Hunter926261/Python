# Check whether a number is a palindrome.

def check_palindrome(num: int) -> bool:
    """
    Checking the number is palindrome or not
    Args:
        num(int): Enter integer value
    Returns: 
        bool: True if palindrome else False
    """

    if not isinstance(num,int):
        raise TypeError("Enter integer value")

    reverse_num = 0
    original_num = num

    while num > 0:
        reverse_num = reverse_num*10 + num%10
        num //= 10

    return original_num == reverse_num

print(check_palindrome(121))