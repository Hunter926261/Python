# count the number of set bits (1s) in the binary representation of a number using bitwise operations

# We will solve this with different methods

# Method 1 : Check each bit using &

def count_set_bit_method_1(num: int) -> int:
    """
    Count's the bit (1s) from the num (after binary converted)
    Args:
        num(int): Enter integer number
    returns:
        int: bit count of 1s
    """

    if not isinstance(num,int):
        raise TypeError("Enter integer number")
    
    if num < 0:
        raise ValueError("Number must be non-negative")

    bit_count = 0
    

    while num:
        if num & 1:
            bit_count += 1
        num >>= 1

    return bit_count

print(count_set_bit_method_1(10))
print(count_set_bit_method_1(13))

# Method 2: Brian Kernighan's Algorithm (Most Efficient) [Interview view importance]

def count_set_bit_method_2(num: int) -> int:
    """
    Count's the bit (1s) from the num (after binary converted)
    Args:
        num(int): Enter integer number
    returns:
        int: bit count of 1s
    """

    if not isinstance(num,int):
        raise TypeError("Enter integer number")
    
    if num < 0:
        raise ValueError("Number must be non-negative")

    bit_count = 0
    
    while num:
        num = num & (num-1)
        bit_count += 1
    
    return bit_count

print(count_set_bit_method_2(11))

# Method 3 (Python Built-in)

num = 16

print(num.bit_count())