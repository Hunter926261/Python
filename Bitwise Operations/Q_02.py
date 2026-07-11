# Multiply by 2 using left shift. 

def Multiply_2(num: int) -> int:
    """
    Multiplying a number by 2 using bitwise left shift
    Args:
        num(int): Enter an interger 
    Returns:
        int: num * 2

    Formula for Multiplication using bitwise left shift:
    x << n = x * 2**n
    """

    if not isinstance(num,int):
        raise TypeError("Number must be integer")
    
    return num << 1

print(Multiply_2(4))
print(Multiply_2(8))
print(Multiply_2(108))
