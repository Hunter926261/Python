# check Armstrong number 

# An Armstrong number is a number that equals the sum of its own digits, where each digit is raised to the power of the total number of digits

def is_armstrong(n):
    original_num = n
    number_digits = 0
    total = 0

    n = original_num
    while n:
        number_digits += 1
        n //= 10

    n = original_num
    while n:
        total += ((n%10)**number_digits)
        n //= 10

    return original_num == total

def main():
    while True:
        try:
            # User input to check Armstrong Number
            n = int(input("Enter n(to check is Armstrong): "))

            if n < 0:
                raise ValueError("n should not be negative")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    is_arm = is_armstrong(n)

    if is_arm:
        print(f"{n} is Armstrong Number")
    else:
        print(f"{n} is not Armstrong Number")




if __name__ == "__main__":
    main()
