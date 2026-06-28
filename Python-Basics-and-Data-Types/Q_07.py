# Build a simple calculator using operators.
# Operations:
# •	Addition 
# •	Subtraction 
# •	Multiplication 
# •	Division 
# •	Modulus 
# •	Floor Division 
# •	Power 


def addition(a,b):
    """
    Arguments: numbers to add
    return: addition of all
    """
    return a+b
    

def subtraction(a,b):
    """
    Arguments: 2 numbers to subtract each other
    return: ex. a - b
    """
    return a-b

def multiplication(a,b):
    """
    Arguments: multiplication of 2 numbers
    return: ex. a * b
    """
    return a*b

def division(a,b):
    """
    Arguments: Division of 2 numbers
    return: ex. a / b
    """
    if b == 0:
        return "divisor can not be 0"
    
    return round(a/b,2)

def modulus(a,b):
    """
    Arguments: Modulus of 2 numbers
    return: ex. a % b
    """
    if b == 0:
        return "Mod can not be found by 0"
    
    return a%b

def floor_division(a,b):
    """
    Arguments: floor_division of 2 numbers
    return: ex. a // b
    """
    if b == 0:
        return "Floor Division can't be found by 0"
    
    return a // b

def power(a,b):
    """
    Arguments: value a and power b
    return: a^b
    """
    return pow(a,b)


print(f"""
    Addition of 1 & 2: {addition(1,2)}
    Subtraction of 3 & 1: {subtraction(3,1)}
    Multiplication of 2 & 5: {multiplication(2,5)}
    Division of 4 & 2: {division(4,2)}
    Modulus of 123 & 10: {modulus(123,10)}
    Floor Division of 123 & 10: {floor_division(123,10)}
    Power of 4 and 3: {power(4,3)}
      """)


