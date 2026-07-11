# Check even/odd using bitwise. 

def check_even_odd(num: int) -> bool:
    """
    Checking the even/odd using bitwise operation
    Args: 
        num(int): Enter an integer number
    Returns:
        bool: True when number is even otherwise False

    Note: 
    Logic - 
        We use Bitwise (&) with 1 because every even number has last bit 0 and odd 1
    """

    if not isinstance(num,int):
        raise TypeError("Number must be integer")
    
    if num & 1 == 0:
        return True
    return False

print(check_even_odd(5))
print(check_even_odd(6))