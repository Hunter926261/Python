# Swap using XOR without 3rd variable

def swap(a:int, b:int) -> tuple[int,int]:
    """
    Swaping 2 variables without using 3rd variable by XOR
    Args:
        a(int): Integer a
        b(int): Integer b
    Returns:
        tuple(int,int): (a,b) 
    Raises:
        TypeError: When a or b is not integer
    """

    if not all(isinstance(x,int) for x in (a,b)):
        raise TypeError("a & b must be integer")

    a ^= b
    b ^= a
    a ^= b

    return a,b

print(swap(2,3))