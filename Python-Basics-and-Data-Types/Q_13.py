# Convert a number into words.
# Example:
# Input:
# 245

# Output:
# Two Four Five

def number_word(num: int) -> str:
    """
    Number to word
    Args:
        num(int): Enter integer
    Returns:
        str: number in words
    Raises:
        TypeError: When value is not integer
    """

    if not isinstance(num,int):
        raise TypeError("Value must be integer")

    WORDS = ["Zero ","One ","Two ","Three ","Four ","Five ","Six ","Seven ","Eight ","Nine "]
    word = ""

    if num < 0:
        word += "Minus "
        
    num = str(abs(num))
    for digit in num:
        word += WORDS[int(digit)]

    return word

print(number_word(-2450))