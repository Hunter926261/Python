#  Check whether a number is an Armstrong Number.
# Armstrong Numbers: 153,1634,etc

def check_armstrong_1(num: int) -> bool:
    """
    Checking is the number is armstrong number or not
    Args:
        num(int): Enter integer number
    Returns:
        bool: True for Armstrong and False for Non-Armstrong number
    Raises:
        TypeError: If num is not integer typeError is raised
    """

    if not isinstance(num,int):
        raise TypeError("Enter integer value")

    count = 0  
    total = 0  
    original = num
    num = abs(num)


    if num == 0:
        count = 1
    
    while num > 0:
        count += 1
        num //= 10

    num = abs(original)

    while num > 0:
        total += pow(num%10,count)
        num //= 10

    return original == total

print(check_armstrong_1(1634))


def check_armstrong_2(num: int) -> bool:
    """
    Checking is the number is armstrong number or not
    Args:
        num(int): Enter integer number
    Returns:
        bool: True for Armstrong and False for Non-Armstrong number
    Raises:
        TypeError: If num is not integer typeError is raised
    """

    if not isinstance(num,int):
        raise TypeError("Enter integer value")

    count = len(str(abs(num)))

    total = 0
    for i in str(abs(num)):
        total += int(i)**count
    
    return total == abs(num)

print(check_armstrong_2(153))