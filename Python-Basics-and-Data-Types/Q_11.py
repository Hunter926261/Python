# Check whether a number is an Automorphic Number (or circular number).
# Automorphic/Circular: An automorphic number (or circular number) is an integer whose square ends with the same digits as the number itself
# ex. 5² = 25 and 76² = 5776

def check_automorphic(num: int) -> bool:
    """
    Check wheather number is Automorphic/Circular number
    Args: 
        num(int): Enter integer value
    Returns: 
        (int): True if the number is Automorphic, otherwise False.
    """

    if not isinstance(num,int):
        raise TypeError("Input must be integer")
    
    if num < 0:
        return False

    square_num = num**2

    return str(square_num).endswith(str(num))

print(check_automorphic(25))
