"""
Reverse a number.
Example:
Input:
12345

Output:
54321
"""


def reverse_number(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    rev_num = 0

    while num>0:
        rev_num = rev_num*10 + num%10
        num //= 10
    
    return sign*rev_num

print(reverse_number(123))