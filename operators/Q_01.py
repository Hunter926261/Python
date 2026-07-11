# 6. Leap year checker. 

# Rules for leap year:
# - It is divisible by 400 → Leap year
# - Otherwise, if it is divisible by 100 → Not a leap year
# - Otherwise, if it is divisible by 4 → Leap year
# - Otherwise → Not a leap year

def is_leap_year(year: int) -> bool:
    """
    Checking is the year is Leap or not
    Args:
        year(int): Enter year
    Returns:
        bool: True if leap else False
    """

    if not isinstance(year,int):
        raise TypeError("Enter year in integer format")

    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    
    return False
    

print(is_leap_year(2024))
print(is_leap_year(2026))
