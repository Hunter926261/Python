# Divide by 2 using right shift. 

def divide_2(num: int) -> int:
    """
    Dividing a number by 2 using bitwise right shift
    Args:
        num(int): Enter an interger 
    Returns:
        int: num / 2

    Formula for Division using bitwise right shift:
    x >> n = x // (2**n)
    """

    if not isinstance(num,int):
        raise TypeError("Number must be integer")
    
    return num >> 1

print(divide_2(4))
print(divide_2(8))
print(divide_2(108))
