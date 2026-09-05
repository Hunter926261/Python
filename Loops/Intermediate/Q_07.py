# Strong Number (also called a Krishnamurthy number or a factorion)

# A Strong Number is a number where the sum of the factorials of its digits equals the original number.

# ex. 145: (1! + 4! + 5! = 1 + 24 + 120 = 145)

def factorial(digit: int) -> int:
    fact = 1

    if digit == 0:
        return 1

    for i in range(2,digit+1):
        fact *= i

    return fact

def is_StrongNumber(n: int) -> bool:
    original_number = n
    sum_digit_fact = 0

    if n == 0:
        return False

    while n:
        sum_digit_fact += factorial(n%10)

        n //= 10

    return original_number == sum_digit_fact

def main():
    while True:
        try:
            n = int(input("Enter n: "))

            if n < 0:
                raise ValueError("n shoud not be negative")

            break
        except ValueError as error:
            print(f"Invalid Input, {error}")

    is_SN = is_StrongNumber(n)

    if is_SN:
        print(f"{n} is strong number")
    else:
        print(f"{n} is not strong number")


if __name__ == "__main__":
    main()