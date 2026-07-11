# Toggle the k-th bit of n

# Formula: n ^ (1 << k)
# where:

# n = number
# k = bit position (0-based indexing from the right)
# 1 << k creates a mask with only the k-th bit set.

def toggle_kth_bit_n(n: int, k: int) -> int:

    if not all(isinstance(x,int) for x in (n,k)):
        raise TypeError("n and k must be non-negative integer")
    
    if any(x < 0 for x in (n,k)):
        raise ValueError("n and k must be non-negative integer")

    return n ^ (1 << k)

print(toggle_kth_bit_n(1,1))